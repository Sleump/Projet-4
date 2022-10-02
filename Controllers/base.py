"""Define the main controller."""
from typing import List
from Models.Player import Player
from Models.Round import Round
from Models.Tournament import Tournament
from Views.base import ViewTournament, ViewPlayer, ViewMatch
from Models.match import Match

player1 = Player("Dupont", "Jean", "28/07/1995", "Male", "71")
player2 = Player("Durant", "Pierre", "28/07/1995", "Male", "72")
player3 = Player("Laval", "Julie", "28/07/1995", "Male", "80")
player4 = Player("alves", "David", "28/07/1995", "Male", "81")
player5 = Player("c", "sept", "28/07/1995", "Male", "84")
player6 = Player("y", "huit", "28/07/1995", "Male", "86")
player7 = Player("b", "jule", "28/07/1995", "Male", "87")
player8 = Player("m", "kelvin", "28/07/1995", "Male", "89")

list_players = [player1, player2, player3, player4, player5, player6, player7, player8]


class Controller:
    """Main controller"""
    dic = {}
    tournament_list = []

    def __init__(self):
        self.views_tournament = ViewTournament()
        self.views_player = ViewPlayer()
        self.views_match = ViewMatch()

    def create_tournament(self):

        name = self.views_tournament.prompt_for_tournament_name()
        place = self.views_tournament.prompt_for_place()
        day = self.views_tournament.prompt_for_day()
        number_of_players = self.views_tournament.prompt_for_players()
        description = self.views_tournament.prompt_for_description()
        time_control = self.views_tournament.prompt_for_time_control()
        Tournament_created = Tournament(name, place, day, number_of_players, description, time_control, rounds)

        return Tournament_created
        # (self, name, place, day, turns, timecontrol, description, players)

    def add_players(self, number_of_players):

        list_players = []

        for _ in range(number_of_players):
            player_name = self.views_player.prompt_for_player_name()
            player_firstname = self.views_player.prompt_for_player_firstname()
            player_birth = self.views_player.prompt_for_player_birth()
            player_gender = self.views_player.prompt_for_player_gender()
            player_rank = self.views_player.prompt_for_player_rank()
            player_score = 0
            player_created = Player(player_name, player_firstname, player_birth, player_gender, player_rank)
            list_players.append(player_created)

        return list_players

    def generate_pairs_one(self, list_players_dur):
        # Entrée: Liste de joueurs
        pairs_round_one = []
        list_players_rank = sorted(list_players_dur, key=lambda Player: Player.rank, reverse=True)
        a = 0
        b = 4

        for pair_player in list_players_dur:
            list_without_current_player = []
            for player in list_players_dur:
                if player.name != pair_player.name:
                    list_without_current_player.append(player)
            self.dic[pair_player.name] = list_without_current_player

        for player in range(4):
            pair = [list_players_rank[a], list_players_rank[b]]
            pairs_round_one.append(pair)
            a += 1
            b += 1
        return pairs_round_one

    def create_matchs(self, player_pairs):

        # Je crée les matchs sous forme de tuple contenant 2 listes contenant joueurs + leur rang
        matchs_first_round = []

        for index, pair in enumerate(player_pairs):
            name_match = f"Match {index}"
            match = Match(pair[0], pair[1], name_match)
            matchs_first_round.append(match)
            self.dic[pair[0].name].remove[pair[1].name]
            self.dic[pair[1].name].remove[pair[0].name]

        return matchs_first_round

    def enter_results_round(self, matchs):

        # Je boucle sur mes matchs:

        for match in matchs:
            # Je sélectionne le premier match pour ensuite l'incrémenter
            view_match = ViewMatch()
            result_match = view_match.prompt_for_player_result(match.list_players)
            match.list_players = result_match
            print(match.list_players)

        return matchs

    def generate_pairs_two(self, list_players_dur):
        # Entrée liste de joueurs
        pairs_round_two = []
        list_players_second_turn = sorted(list_players_dur, key=lambda Player: Player.score, reverse=True)

        a = 0
        b = 1
        for i in range(4):

            # [player 1 : obj Pierre (20), player 2: obj Alex (5), player 3: obj Thomas (10)]
            player = list_players_second_turn[i]

            copy_list_players_second_turn = list_players_second_turn.copy()
            copy_list_players_second_turn.remove(player)

            # [player 2: obj Alex (5), player 3: obj Thomas (10)]
            list_players_second_turn = sorted(copy_list_players_second_turn, key=lambda Player: Player.score,
                                              reverse=True)

            # [player 3: obj Thomas (10), player 2: obj Alex (5)]
            pair = [player]

            # Find a user to play with (should not play again with a previous one)
            other_players_to_play_with = self.dic[player.username]

            # 1
            for player in list_players_second_turn:
                if player.username in other_players_to_play_with:
                    pair.append(player)
                    break
                else:
                    continue

            assert len(pair) == 2

            pairs_round_two.append(pair)

            # initial other_players_to_play_with = [Alex, Thomas, Pierre]

            # expected other_players_to_play_with = [Alex, Thomas, Pierre]

            pairs_round_two.append(pair)
            a += 1
            b += 1
        return pairs_round_two

    def generate_matchs_round_two(self, pairs_of_players: list) -> List[Match]:

        list_players_dur = [player1, player2, player3, player4, player5, player6, player7, player8]
        # J'ordonne du plus grand au plus petit la liste de joueurs basé sur le score 1er tour
        list_players_second_turn = sorted(list_players_dur, key=lambda x: x.player_score, reverse=True)

        matchs_round_two = []
        for match in range(4):
            a = 0
            b = 1
            match_one_round_two = [(list_players_dur[a], list_players_dur[a].score),
                                   (list_players_dur[b], list_players_dur[b].score)]
            a = a + 1
            b = b + 1
            # if match_one_round_two == "match du 1er tour":# soit match_one
            # b = b + 1
        matchs_round_two.append(match_one_round_two)

        return matchs_round_two

    def choice_create_tournament(self):

        list_of_players = []
        list_of_players_basics = []
        # Afficher menu principal avec 2 options : créer un tournoi et afficher les rapports
        # L'utilisateur choisit une option
        # Option 1 " Créer un tournoi " : Renseigner les informations du tournoi via input

        new_tournament = self.create_tournament()
        list_of_players = self.add_players(new_tournament.number_of_players)
        list_of_players_basics.append(list_of_players)
        pairs = self.generate_pairs_one(list_of_players)

        rounds = []

        for index in range(4):
            print(len(rounds))
            if index == 0:
                pairs = self.generate_pairs_one(list_of_players)
                matchs = self.create_matchs(pairs)
                print("Les matchs sont :", matchs)
                refreshed_matchs = self.enter_results_round(matchs)
                print("Les matchs actualisés sont :", refreshed_matchs)
                round_name = f"Round {index}"
                round = Round(matchs, round_name)
                rounds.append(round)


            else:
                pairs_two = self.generate_pairs_two(list_of_players)
                matchs_two = self.create_matchs(pairs_two)
                print("Les matchs du " + round_name + " sont :", matchs_two)
                refreshed_matchs_two = self.enter_results_round(matchs_two)
                print("Les matchs actualisés sont :", refreshed_matchs_two)
                round_name = f"Round {index}"
                round_two = Round(matchs_two, round_name)
                rounds.append(round)

            print("+++++++")
        print(rounds)
        new_tournament.rounds = rounds
        print(new_tournament.rounds)
        self.tournament_list.append(new_tournament.name)

controller = Controller()


def run(self):
    choice: str = ""

    while True:
        print("1) Créer un tournoi")
        print("2) Consulter les rapports")
        print("3) Quitter le programme")
        choice = input("Ecrivez un choix: ")

        choice = choice.strip()

    if (choice == "1"):
        run()

    elif (choice == "2"):

        for tournament in enumerate(tournament_list):
            print(index, ")", new_tournament.name)

            choice = input("Ecrivez un choix: ")
            choice = choice.strip()

            if (choice == index):
                print(self.tournament_list[index].name, self.tournament_list[index].rounds)
                #sort players alphabetically
                players_tournament_alphabetically = sorted(self.tournament.list_players)
                #print(players_tournament_alphabetically)


    elif (choice == "3"):
        variable = 1

    return


controller = Controller()
controller.run()