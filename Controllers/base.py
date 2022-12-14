"""Define the main controller."""
from datetime import datetime
from tinydb import TinyDB
import os
from Models.Player import Player
from Models.Round import Round
from Models.Tournament import Tournament
from Views.base import ViewTournament, ViewPlayer, ViewMatch
from Models.match import Match






class Controller:

    db = TinyDB('rapport.json')

    """Main controller"""
    pairs_of_tournament = []

    tournament_list = []

    players_of_all_time = []
    list_of_rounds = []
    list_of_players = []


    def __init__(self):
        self.views_tournament = ViewTournament()
        self.views_player = ViewPlayer()
        self.views_match = ViewMatch()


    def create_tournament(self):

        name = self.views_tournament.prompt_for_tournament_name()
        place = self.views_tournament.prompt_for_place()
        day = self.views_tournament.prompt_for_day()
        number_of_players = 8
        players = self.list_of_players
        #number_of_players = self.views_tournament.prompt_for_players()
        description = self.views_tournament.prompt_for_description()
        time_control = self.views_tournament.prompt_for_time_control()
        list_of_rounds = self.list_of_rounds

        tournament_created = Tournament(name, place, day, number_of_players, players, description, time_control, list_of_rounds)

        return tournament_created


    def add_players(self):


        for _ in range(8):
            player_name = self.views_player.prompt_for_player_name()
            player_firstname = self.views_player.prompt_for_player_firstname()
            player_birth = self.views_player.prompt_for_player_birth()
            player_gender = self.views_player.prompt_for_player_gender()
            player_rank = self.views_player.prompt_for_player_rank()
            player_score = 0
            player_created = Player(player_name, player_firstname, player_birth, player_gender, player_rank)
            self.list_of_players.append(player_created)

        return self.list_of_players

    def generate_pairs_one(self):
        # Entr??e: Liste de joueurs

        pairs_round_one = []

        list_players_rank = sorted(self.list_of_players, key=lambda Player: Player.rank, reverse=True)
        firsts_elements = list_players_rank[0:4]
        second_elements = list_players_rank[4:]


        for i in range(4):

            pair = (firsts_elements[i], second_elements[i])
            pairs_round_one.append(pair)
            self.pairs_of_tournament.append(pair)

        return pairs_round_one

    def create_matchs(self, player_pairs):

        # Je cr??e les matchs sous forme de tuple contenant 2 listes contenant joueurs + leur rang
        matchs_first_round = []


        for index, pair in enumerate(player_pairs):
            name_match = f"Match {index}"
            match = Match(player1 = pair[0], player2 = pair[1], name = name_match)
            #                        pair[0], pair[1]
            matchs_first_round.append(match)

        return matchs_first_round

    def enter_results_round(self, matchs):

        # Je boucle sur mes matchs:

        for match in matchs:
            # Je s??lectionne le premier match pour ensuite l'incr??menter
            view_match = ViewMatch()
            result_match = view_match.prompt_for_player_result(match.list_players)
            match.list_players = result_match
            print("matchs.list_players =", match.list_players)

        return matchs

    def generate_pairs_two(self, list_of_players):
        # Entr??e liste de joueurs
        pairs_round_two = []
        list_players_second_turn = sorted(list_of_players, key=lambda Player: Player.score, reverse=True)
        print(list_players_second_turn)
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

    def insertion(self):

        db = TinyDB('rapport.json')

        players_serialized = []
        rounds_serialized = []

        for player in self.list_of_players:

            player_to_save = {
                "name" : player.username,
                "birth" : player.birth,
                "gender" : player.gender,
                "rank" : player.rank,
                "score" : player.score,

            }
            db.insert(player_to_save)





    def choice_create_tournament(self):



        # Afficher menu principal avec 2 options : cr??er un tournoi et afficher les rapports
        # L'utilisateur choisit une option
        # Option 1 " Cr??er un tournoi " : Renseigner les informations du tournoi via input

        new_tournament = self.create_tournament()
        self.list_of_players = self.add_players()
        new_tournament.players = self.list_of_players

        #self.list_of_players = self.add_players(new_tournament.number_of_players)
        # A supprimer ? pairs = self.generate_pairs_one(list_of_players)



        for index in range(4):

            print("taille des rounds", len(self.list_of_rounds))

            if index == 0:
                round_count = 1
                pairs = self.generate_pairs_one()
                matchs = self.create_matchs(pairs)
                begin_time = datetime.now()
                print("Les matchs sont :", matchs, "d??but du round ??:", begin_time)
                refreshed_matchs = self.enter_results_round(matchs)
                print("Les matchs actualis??s sont :", refreshed_matchs)
                round_name = f"Round {round_count}" # {matchs} ?
                end_time = datetime.now()
                print("Fin du round", end_time)
                round_one = Round(matchs, round_name, begin_time, end_time)
                print(" round_one", round_one)
                self.list_of_rounds.append(round_one)
                round_count += 1

            else:
                pairs_two = self.generate_pairs_two(self.list_of_players)
                matchs_two = self.create_matchs(pairs_two)
                begin_time = datetime.now()
                print("Les matchs du " + round_name + " sont :", matchs_two, "d??but du round ??:", begin_time)
                refreshed_matchs_two = self.enter_results_round(matchs_two)
                print("Les matchs actualis??s sont :", refreshed_matchs_two)
                round_name = f"Round {round_count}"
                end_time = datetime.now()
                print("Fin du round", end_time)
                round_two = Round( matchs = matchs_two, name = round_name, begin_time = begin_time, end_time = end_time)
                print("round_two", round_two)
                self.list_of_rounds.append(round_two)
                print("list_of_round", new_tournament.list_of_rounds)
                round_count += 1

            print("Passage ?? un autre round")



        self.tournament_list.append(new_tournament)
        self.players_of_all_time.append(self.list_of_players)
        self.insertion()
        self.menu()


    def menu(self):

        print("Bienvenue sur votre logiciel de gestion de tournois d'??chec")
        print("Choisissez une option:")

        os.system('cls')

        choice: str = ""

        while True:
            print("1) Cr??er un tournoi")
            print("2) Consulter les rapports")
            print("3) Quitter le programme")
            print("4 Modifier le rang d'un joueur")
            choice = input("Ecrivez un choix: ")

            choice = choice.strip()

            if (choice == "1"):
                self.choice_create_tournament()

            elif (choice == "2"):

                for index, tournament in enumerate(self.tournament_list):
                    print(index, ")", tournament.name)

                choice = input("Choisissez le tournoi ?? afficher: ")



                if choice == str(index):

                    print(self.tournament_list[index].name, self.tournament_list[index].rounds)

                    # sort players alphabetically:
                    players_tournament_alphabetically = sorted(self.tournament_list[index].list_of_players, key=lambda x: x.player.name)
                    print("Les joueurs du tournoi class?? par ordre alphab??tique sont :", players_tournament_alphabetically)

                    # sort players by score:
                    player_tournament_score = sorted(self.tournament_list[index].players, key=lambda x: x.player.score)
                    print("Les joueurs du tournoi class?? par ordre alphab??tique sont :",
                          player_tournament_score)

                        # print(players_tournament_alphabetically)


                elif (choice == "3"):

                    break
                """
                elif (choice == "4"):
                    
                    print("Taper le nom du joueurs dont vous souhaitez modifier le rang")
                    player_selected_rank = input("")
                    new_rank = input("Tapez le nouveau rang:")
                    player_selectezd_rank.rank = new_rank
                
                """


    def run(self):

        self.menu()




controller = Controller()
controller.run()