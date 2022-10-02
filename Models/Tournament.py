class Tournament:
    players = []
    rounds = []

    def __init__(self, name, place, day, timecontrol, description, players):
        self.name = name
        self.place = place
        self.day = day
        self.timecontrol = timecontrol
        self.description = description
        self.players = players
        self.number_of_players = 8
