from tinydb import TinyDB, Query





db = TinyDB('db.json')

User = Query()
class Player:

    def __init__(self, name):
        self.name = name


def insert():

    player1 = Player("Jean")
    player2 = Player("Louis")
    player3 = Player("David")

    joueurs = [player1, player2, player3]
    joueurs_serialised = []
    for joueur in joueurs :

        player_to_save = {
            "name": joueur.name,
        }

        joueurs_serialised.append(player_to_save)



    age = 28
    dico = {"coucou": "hello"}
    db.insert({'name': 'John', 'age': age})
    db.insert({'name': 'Max', 'age': 25})
    db.insert({'name': 'Sarah', 'age': 21, 'city': 'New York'})
    db.insert({"joueurs":joueurs_serialised})
def search():
    results = db.search(User.city == 'New York')
    print(results)


insert()
#search()
print(db.all())

"""
db = TinyDB('db.json')
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age




player = Player(name='John', age=22)

serialized_player = {
    'name': player.name,
    'age': player.age
}

name = serialized_player['name']
age = serialized_player['age']
player = Player(name=name, age=age)

players_table = db.table('players')
players_table.truncate()	# clear the table first
players_table.insert_multiple(serialized_player)



        for round in self.list_of_rounds:

            round_to_save = {
                "matchs" : round.matchs,
                "name" : round.name,
                "begin_time" : round.begin_time,
                "end_time" : round.end_time,
            }
            rounds_serialized.append(round_to_save)


        tournament_to_save = {
            "name" : new_tournament.name,
            "place" : new_tournament.place,
            "day" : new_tournament.day,
            "timecontrol" : new_tournament.timecontrol,
            "description" : new_tournament.description,
            "players" : players_serialized,
            "number_of_players" : 8,
            "list_of_rounds" : rounds_serialized,
        }







"""
""""
    def modify_player(self, player_selected):

        #Choisir le joueur à modifier:

        player_selected = input("Tapez le nom et prénom du joueur souhaité:")


        #Chercher le joueur:

        User = Query()

        results = db.search(User.username == player_selected)

        print("Joueur trouvé:", results, "tapez son nouveau rang:")
        #ATTENTION JSON DONC DICTIONNAIRE  player_selected["score"] = 2.5
        new_rank = input("Tapez le nouveau score:")
        player_selected.score = float(new_rank)
        print("Le nouveau score du joueur", player_selected, "est:", new_rank.score)



"""