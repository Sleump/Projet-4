

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



