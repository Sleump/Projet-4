class Tournament:
    players = []
    rounds = []

    def __init__(self, name, place, day, timecontrol, description, players, number_of_players, list_of_rounds):
        self.name = name
        self.place = place
        self.day = day
        self.timecontrol = timecontrol
        self.description = description
        self.players = players
        self.number_of_players = number_of_players
        self.list_of_rounds = list_of_rounds

    def __repr__(self):
        return f"{self.name}"


