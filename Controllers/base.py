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
    compteur = 1
    players_of_all_time = []
    list_of_rounds = []
    list_of_players = []
    number_of_players = 8

    def __init__(self):
        self.views_tournament = ViewTournament()
        self.views_player = ViewPlayer()
        self.views_match = ViewMatch()

    def create_tournament(self):

        name = self.views_tournament.prompt_for_tournament_name()
        place = self.views_tournament.prompt_for_place()
        day = self.views_tournament.prompt_for_day()
        time_control = self.views_tournament.prompt_for_time_control()
        description = self.views_tournament.prompt_for_description()
        list_of_players = self.list_of_players
        list_of_rounds = self.list_of_rounds
        number_of_players = self.number_of_players



        tournament_created = Tournament(name , place, day, time_control, description, list_of_players, list_of_rounds, number_of_players)

        return tournament_created

    def add_players(self):

        for _ in range(8):
            player_name = self.views_player.prompt_for_player_name()
            player_firstname = self.views_player.prompt_for_player_firstname()
            player_birth = self.views_player.prompt_for_player_birth()
            player_gender = self.views_player.prompt_for_player_gender()
            player_rank = self.views_player.prompt_for_player_rank()
            player_score = 0
            player_created = Player(player_name, player_firstname, player_birth, player_gender, player_rank, player_score)
            self.list_of_players.append(player_created)


        return self.list_of_players

    def generate_pairs_one(self):

        # Entrée: Liste de joueurs

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

        # Je crée les matchs sous forme de tuple contenant 2 listes contenant joueurs + leur rang
        matchs_first_round = []

        for index, pair in enumerate(player_pairs):
            name_match = f"Match {index}"
            match = Match(player1=pair[0], player2=pair[1], name=name_match)
            #                        pair[0], pair[1]
            matchs_first_round.append(match)

        return matchs_first_round

    def enter_results_round(self, matchs):

        # Je boucle sur mes matchs

        for match in matchs:
            # Je sélectionne le premier match pour ensuite l'incrémenter
            view_match = ViewMatch()
            result_match = view_match.prompt_for_player_result(match.list_players)
            match.list_players = result_match
            print("matchs.list_players =", match.list_players)

        return matchs

    def generate_pairs_two(self, list_of_players):
        # Entrée liste de joueurs
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

    def insertion(self, new_tournament):

        db = TinyDB('rapport.json')

        players_serialized = []
        rounds_serialized = []

        for player in self.list_of_players:

            player_to_save = {
                "name": player.username,
                "birth": player.birth,
                "gender": player.gender,
                "rank": player.rank,
                "score": player.score,

            }
            players_serialized.append(player_to_save)
            self.players_of_all_time.append(player_to_save)

        for round in self.list_of_rounds:

            round_to_save = {
                "matchs": round.matches,
                "name": round.name,
                "begin_time": round.begin_time,
                "end_time": round.end_time,
            }
            rounds_serialized.append(round_to_save)

        tournament_to_save = {
            "name": new_tournament.name,
            "place": new_tournament.place,
            "day": new_tournament.day,
            "timecontrol": new_tournament.timecontrol,
            "description": new_tournament.description,
            "players": [str(player) for player in players_serialized],
            "number_of_players": 8,
            "list_of_rounds": [str(round) for round in rounds_serialized],
        }

        return tournament_to_save
        #db.insert(tournament_to_save)

    def custom_input(message):

        response = input(f'(s) (pour sauvegarder)\n(q) (pour quitter)\n\n{"*" * 10}\n{message}')

        return response

    def choice_create_tournament(self):

        # Afficher menu principal avec 2 options : créer un tournoi et afficher les rapports
        # L'utilisateur choisit une option
        # Option 1 " Créer un tournoi " : Renseigner les informations du tournoi via input

        new_tournament = self.create_tournament()
        print("+++++++++++")
        print(new_tournament.name , new_tournament.place, new_tournament.day, new_tournament.timecontrol, new_tournament.description, new_tournament.list_of_players, new_tournament.list_of_rounds, new_tournament.number_of_players)
        new_tournament.list_of_players = self.add_players()
        print(new_tournament.name , new_tournament.place, new_tournament.day, new_tournament.timecontrol, new_tournament.description, new_tournament.list_of_players, new_tournament.list_of_rounds, new_tournament.number_of_players)
        #new_tournament.players = self.list_of_players

        # self.list_of_players = self.add_players(new_tournament.number_of_players)
        # A supprimer ? pairs = self.generate_pairs_one(list_of_players)

        for index in range(4):

            print("taille des rounds", len(self.list_of_rounds))

            if index == 0:
                round_count = 1
                pairs = self.generate_pairs_one()
                matchs = self.create_matchs(pairs)
                begin_time = datetime.now()
                print("Les matchs sont :", matchs, "début du round à:", begin_time)
                refreshed_matchs = self.enter_results_round(matchs)
                print("Les matchs actualisés sont :", refreshed_matchs)
                round_name = f"Round {round_count}"
                end_time = datetime.now()
                print("Fin du round", end_time)
                round_one = Round(matches=matchs, name=round_name, begin_time=begin_time, end_time=end_time)
                print(" round_one", round_one)
                self.list_of_rounds.append(round_one)
                print(new_tournament.name, new_tournament.place, new_tournament.day, new_tournament.list_of_players,
                      new_tournament.description, new_tournament.timecontrol, new_tournament.list_of_rounds,
                      new_tournament.number_of_players)
                round_count += 1

            else:
                round_count = 2
                pairs_two = self.generate_pairs_two(self.list_of_players)
                matchs_two = self.create_matchs(pairs_two)
                begin_time = datetime.now()
                print("Les matchs du " + round_name + " sont :", matchs_two, "début du round à:", begin_time)
                refreshed_matchs_two = self.enter_results_round(matchs_two)
                print("Les matchs actualisés sont :", refreshed_matchs_two)
                round_name = f"Round {round_count}"
                end_time = datetime.now()
                print("Fin du round", end_time)
                round_two = Round(matches=matchs_two, name=round_name, begin_time=begin_time, end_time=end_time)
                print("round_two", round_two)
                self.list_of_rounds.append(round_two)
                print(new_tournament.name, new_tournament.place, new_tournament.day, new_tournament.list_of_players,
                      new_tournament.description, new_tournament.timecontrol, new_tournament.list_of_rounds,
                      new_tournament.number_of_players)

                round_count += 1

            print("Passage à un autre round")

        self.tournament_list.append(new_tournament)

        tournament_saved =self.insertion(new_tournament)
        print(tournament_saved)

        self.db.insert({f"Tournoi {self.compteur}": tournament_saved})
        self.compteur += 1
        self.menu()

    def menu(self):

        print("Bienvenue sur votre logiciel de gestion de tournois d'échec")
        print("Choisissez une option:")

        os.system('cls')

        choice: str = ""

        while True:
            print("1) Créer un tournoi")
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

                choice = input("Choisissez le tournoi à afficher: ")

                if choice == str(index):

                    print(self.tournament_list[index].name, self.tournament_list[index].rounds)

                    # sort players alphabetically:
                    players_tournament_alphabetically = sorted(self.tournament_list[index].list_of_players,
                                                               key=lambda x: x.player.name)
                    print("Les joueurs du tournoi classé par ordre alphabétique sont :",
                          players_tournament_alphabetically)

                    # sort players by score:
                    player_tournament_score = sorted(self.tournament_list[index].list_of_players, key=lambda x: x.player.score)
                    print("Les joueurs du tournoi classé par ordre alphabétique sont :",
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
