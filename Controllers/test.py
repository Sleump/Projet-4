
"""
class Tournament:
    def __init__(self, name, rounds, matches):
        self.name = name
        self.rounds = rounds
        self.matches = matches
class Match:

    def __init__(self, name,  players):
        self.players = players
        self.name = name


    def __repr__(self):
        return f"{self.players}"

matches = Match("Le Match", ["Luc", "Paul"])
tournament_created = Tournament("Paris", rounds = [3, 2, 1], matches = matches)

print(tournament_created.matches)



class Player:

    def __init__(self, name, firstname, birth, gender, rank, score)
        self.name = name  # player_name
        self.firstname = firstname  # player_firstname
        self.birth = birth  # player_birth
        self.gender = gender  # player_gender
        self.rank = rank  # player_rank
        self.score = score  # player_score
        self.username = self.firstname + ' ' + self.name


player1 = Player("Dupont", "Jean", "28/07/1995", "Male", 71, 0)
player2 = Player("Durant", "Pierre", "28/07/1995", "Male", 72, 0)
player3 = Player("Laval", "Julie", "28/07/1995", "Male", 80, 0)
player4 = Player("alves", "David", "28/07/1995", "Male", 81, 0)
player5 = Player("c", "sept", "28/07/1995", "Male", "84")
player6 = Player("y", "huit", "28/07/1995", "Male", "86")
player7 = Player("b", "jule", "28/07/1995", "Male", "87")
player8 = Player("m", "kelvin", "28/07/1995", "Male", "89")

list_players = [player1, player2, player3, player4, player5, player6, player7, player8]


def generate_pairs_one(self, list_players):
    # Entree: Liste de joueurs
    pairs_round_one = []
    list_players_rank = sorted(list_players, key=lambda Player: Player.rank, reverse=True)
    a = 0
    b = 4

    for pair_player in list_players:
        list_without_current_player = []
        for player in list_players:
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
        match = Match(player1 = pair[0], player2 = pair[1], name = name_match)
        #                            pair[0], pair[1]
        matchs_first_round.append(match)
        print(matchs_first_round)
        pair[0].pop(pair[1])
         pair[1].pop(pair[0])
        #self.dic[pair[0].name].remove[pair[1].name]
        #self.dic[pair[1].name].remove[pair[0].name]

        return matchs_first_round



#Je copie la liste des pairs de joueurs du tour 1 :
pairs_copied_list = pairs.copy()

# A la création de la pair du deuxième tour , effectuer la vérification:

list_players_second_turn = sorted(list_players_dur, key=lambda Player: Player.score, reverse=True)

for player in range(4):
    pair = [list_players_rank[a], list_players_rank[b]]
    if (pair in pairs_copied_list):
        b += 1
        pair = [list_players_rank[a], list_players_rank[b]]
        pairs_round_two.append(pair)
        a += 1
        b += 1
    else:
        pair = [list_players_rank[a], list_players_rank[b]]
        pairs_round_one.append(pair)
        a += 1
        b += 1
        pairs_round_two.append(pair)

"""

list