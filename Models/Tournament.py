class Tournament:

    rounds = []

    def __init__(self, name, place, day, timecontrol, description, list_of_players, list_of_rounds, number_of_players):
        self.name = name
        self.place = place
        self.day = day
        self.timecontrol = timecontrol
        self.description = description
        self.list_of_players = list_of_players
        self.list_of_rounds = list_of_rounds
        self.number_of_players = number_of_players

    def __repr__(self):
        return f"{self.name}"


