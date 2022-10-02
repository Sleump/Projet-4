from Models.Player import Player
from Models.match import Match
from Views.base import ViewMatch
"""
player1 = Player("Dupont", "Jean", "28/07/1995", "Male", 71, 0)
player2 = Player("Durant", "Pierre", "28/07/1995", "Male", 72, 0)
player3 = Player("Laval", "Julie", "28/07/1995", "Male", 80, 0)
player4 = Player("Alves", "David", "28/07/1995", "Male", 81, 0)
player5 = Player("Silva", "John", "28/07/1995", "Male", 84, 0)
player6 = Player("Goncalves", "Guillaume", "28/07/1995", "Male", 86, 0)
player7 = Player("Dagobert", "Jule", "28/07/1995", "Male", 87, 0)
player8 = Player("Calvas", "kelvin", "28/07/1995", "Male", 89, 0)



list_players_dur = [player1, player2, player3, player4, player5, player6, player7, player8]
pairs_round_one = []
matchs_first_round = []
pairs_round_two = []
matchs_second_round = []


def generate_pairs_one(list_players_dur):
    #Entrée: Liste de joueurs
    list_players_rank = sorted(list_players_dur, key=lambda Player: Player.rank, reverse=True)
    a = 0
    b = 4
    for player in range(4):

        pair = [list_players_rank[a], list_players_rank[b]]
        pairs_round_one.append(pair)
        a += 1
        b += 1
    return pairs_round_one
player_pairs = generate_pairs_one()
print(player_pairs)


   def create_matchs(self, player_pairs):

        # Je crée les matchs sous forme de tuple contenant 2 listes contenant joueurs + leur rang
        matchs_first_round = []

        for index, pair in enumerate(player_pairs):
            name_match = f"Match {index}"
            match = Match(pair[0], pair[1], name_match)
            matchs_first_round.append(match)
            self.dic[pair[0].name].remove[pair[1].name]
            self.dic[pair[1].name].remove[pair[0].name]

matchs_round_one = create_matchs(player_pairs)
print("Les matchs sont :", matchs_round_one)




def enter_results_round(matchs):
    # Entrée : liste de joueurs

    # list ordonnée par rang = [player8, player7, player6, player5, player4, player3, player2, player1]
    #list_ordonate = sorted(list_players_dur, key=lambda Player: Player.rank, reverse=True)

    # Les matchs sont :
    # matchs = [player8, player4] et [player7, player3] et [player6, player2] et [player5, player1]

    # Voici les scores de chaque joueur :
    # Je boucle sur mes matchs:

    for match in matchs:
        #Je sélectionne le premier match pour ensuite l'incrémenter
        view_match = ViewMatch()
        result_match = view_match.prompt_for_player_result(match.list_players)
        match.list_players = result_match
        print(match.list_players)

    return matchs



results = enter_results_round(matchs_round_one)
print(results)
for result in results:
    print(result.list_players)




def generate_pairs_two:
    #Entrée liste de joueurs
    list_players_second_turn = sorted(list_players_dur, key=lambda Player: Player.score, reverse=True)
    a = 0
    b = 1
    for player in range(4):
        pair = [list_players_second_turn[a], list_players_second_turn[b]]
        pairs_round_two.append(pair)
        a += 1
        b += 1
    return pairs_round_two



    def run(self):



        list_of_players = []
        list_of_players_basics = []
        # Afficher menu principal avec 2 options : créer un tournoi et afficher les rapports
        # L'utilisateur choisit une option
        # Option 1 " Créer un tournoi " : Renseigner les informations du tournoi via input

        new_tournament = self.create_tournament()
        list_of_players = self.add_players(new_tournament.number_of_players)
        list_of_players_basics.append(list_of_players)
        pairs = self.generate_pairs_one(list_of_players)
        print(new_tournament.number_of_players)
        matchs = self.create_matchs(pairs)
        print("Les matchs sont :", matchs)
        refreshed_matchs = self.enter_results_round(matchs)
        print("Les matchs actualisés sont :", refreshed_matchs)
        rounds = []
        for result in refreshed_matchs:
            print(result.list_players)

        #Turn2
        pairs_two = self.generate_pairs_two(list_of_players)
        matchs_two = self.create_matchs(pairs_two)
        print("Les matchs du tour 2 sont :", matchs_two)
        refreshed_matchs_two = self.enter_results_round(matchs_two)
        print("Les matchs actualisés sont :", refreshed_matchs_two)

        for result in refreshed_matchs_two:
            print(result.list_players)



        for _ in range(4):
            pairs = self.generate_pairs_one(list_of_players)
            matchs = self.create_matchs(pairs)
            print("Les matchs sont :", matchs)
            refreshed_matchs = self.enter_results_round(matchs)
            print("Les matchs actualisés sont :", refreshed_matchs)
            round = Round(matchs)
            rounds.append(round)


            if refreshed_matchs:
                pairs_two = self.generate_pairs_two(list_of_players)
                matchs_two = self.create_matchs(pairs_two)
                print("Les matchs du tour 2 sont :", matchs_two)
                refreshed_matchs_two = self.enter_results_round(matchs_two)
                print("Les matchs actualisés sont :", refreshed_matchs_two)
                round2 =Round(matchs_two)
                rounds.append(round)

        for index, round in enumerate(rounds):
            round_name = f"Round{index}

controller = Controller()
controller.run()
"""


