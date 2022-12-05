from tinydb import TinyDB, Query

"""
class Tournament:
    def __init__(self, name, rounds ):
        self.name = name
        self.rounds = rounds



class Round:
    def __init__(self, matches):
        self.matches = matches



class Match:

    def __init__(self, name,  players):
        self.name = name
        self.players = players



    def __repr__(self):
        return f"{self.players}"

matches = Match("Le Match", ["Luc", "Paul"])
rounds = Round(matches)
tournament_created = Tournament("Paris", rounds = rounds)

print(tournament_created.rounds)


class Player:

    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score

    def points(self, points):
        self.score += points

    def __repr__(self):
        return f"{self.player_name}"


player = Player( player_name = "David", score = 0)

question = input("Tapez le score du joueur :")

player.points(int(question))
print(player.score)



db = TinyDB('db.json')

User = Query()

def insert():
    db.insert({'name': 'John', 'age': 28})
    db.insert({'name': 'Max', 'age': 25})
    db.insert({'name': 'Sarah', 'age': 21, 'city': 'New York'})

def search():
    results = db.search(User.city == 'New York')
    print(results)

db.purge("2")
#insert()
#search()
print(db.all())

"""

def multiply():
    return 5 * 5

resultat = multiply()

print(" Le résultat est", resultat)

def multiply2(n):
    return n * 5


print(" Le résultat est", multiply2(6))