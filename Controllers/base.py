"""Define the main controller."""
import os
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
    pairs_of_tournament = []
    round_zero = Tournament("zero", "paris", "2/09/21", "30", "great", 8, [])
    tournament_list = [round_zero]
    round_zero.rounds = "ça fonctionne"
    players_of_all_time = []


    def __init__(self):
        self.views_tournament = ViewTournament()
        self.views_player = ViewPlayer()
        self.views_match = ViewMatch()
        self.rounds = None

    def create_tournament(self):

        name = self.views_tournament.prompt_for_tournament_name()
        place = self.views_tournament.prompt_for_place()
        day = self.views_tournament.prompt_for_day()
        number_of_players = self.views_tournament.prompt_for_players()
        description = self.views_tournament.prompt_for_description()
        time_control = self.views_tournament.prompt_for_time_control()
        rounds = self.rounds
        tournament_created = Tournament(name, place, day, number_of_players, description, time_control, rounds)

        return tournament_created
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
            player_created = Player(player_name, player_firstname, player_birth, player_gender, player_rank, player_score)
            list_players.append(player_created)

        return list_players

    def generate_pairs_one(self, list_players_dur):
        # Entrée: Liste de joueurs
        pairs_round_one = []
        list_players_rank = sorted(list_players_dur, key=lambda Player: Player.rank, reverse=True)
        print("Liste player rank = ", list_players_rank)
        a = 0
        b = 4
        for i in list_players_rank:
            pair = [list_players_rank[a], list_players_rank[b]]
            pairs_round_one.append(pair)
            self.pairs_of_tournament.append(pair)
            a += 1
            b += 1
            print("les pairs de joueurs sont", pairs_round_one)


            return pairs_round_one

    def create_matchs(self, player_pairs):

        # Je crée les matchs sous forme de tuple contenant 2 listes contenant joueurs + leur rang
        matchs_first_round = []


        for index, pair in enumerate(player_pairs):
            name_match = f"Match {index}"
            match = Match(player1 = pair[0], player2 = pair[1], name = name_match)
            #                        pair[0], pair[1]
            matchs_first_round.append(match)
            print(matchs_first_round)



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
        for player in range(4):
            pair = [list_players_second_turn[a], list_players_second_turn[b]]
            if pair in self.pairs_of_tournament:
                a = 0
                b = 2
                pair = [list_players_second_turn[a], list_players_second_turn[b]]
                pairs_round_two.append(pair)
                self.pairs_of_tournament.append(pair)
                b = 1

            else:
                pairs_round_two.append(pair)
                self.pairs_of_tournament.append(pair)
            a += 1
            b += 1
            print(pairs_round_two)



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
        # A supprimer ? pairs = self.generate_pairs_one(list_of_players)

        self.rounds = []

        for index in range(4):
            print(len(self.rounds))
            if index == 0:
                index_veridique = index + 1
                pairs = self.generate_pairs_one(list_of_players)
                matchs = self.create_matchs(pairs)
                print("Les matchs sont :", matchs)
                refreshed_matchs = self.enter_results_round(matchs)
                print("Les matchs actualisés sont :", refreshed_matchs)
                round_name = f"Round {index_veridique}" # {matchs} ?
                round = Round(matchs, round_name)
                self.rounds.append(round)


            else:
                pairs_two = self.generate_pairs_two(list_of_players)
                matchs_two = self.create_matchs(pairs_two)
                print("Les matchs du " + round_name + " sont :", matchs_two)
                refreshed_matchs_two = self.enter_results_round(matchs_two)
                print("Les matchs actualisés sont :", refreshed_matchs_two)
                round_name = f"Round {index}"
                round_two = Round( matchs = matchs_two, name = round_name)
                self.rounds.append(round_two)

            print("Passage à un autre round")
        print(self.rounds)
        new_tournament.rounds = self.rounds
        print(new_tournament.rounds)
        self.tournament_list.append(new_tournament)
        self.players_of_all_time.append(list_of_players_basics)
        self.menu()

    def menu(self):

        os.system('cls')

        choice: str = ""

        while True:
            print("1) Créer un tournoi")
            print("2) Consulter les rapports")
            print("3) Quitter le programme")
            choice = input("Ecrivez un choix: ")

            choice = choice.strip()

            if (choice == "1"):
                self.choice_create_tournament()

            elif (choice == "2"):

                for index, tournament in enumerate(self.tournament_list):
                    print(index, ")", tournament.name)

                choice = input("Choisissez le tournoi à afficher: ")

                print("TEST", type(index))
                print("TEST", type(choice))

                if choice == str(index):

                    print(self.tournament_list[index].name, self.tournament_list[index].rounds)
                    # sort players alphabetically
                    players_tournament_alphabetically = sorted(self.tournament_list[index].list_players, key=lambda x: x.player.name)
                    print("Les joueurs du tournoi sont :", players_tournament_alphabetically)


                        # print(players_tournament_alphabetically)


                elif (choice == "3"):
                    break



    def run(self):

        self.menu()




controller = Controller()
controller.run()