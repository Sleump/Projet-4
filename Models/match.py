class Match:
    def __init__(self, player1, player2, name):
        self.list_players = ([player1, player1.score], [player2, player2.score])  #     0 => score joueur initialisé au début
        self.name = name

    def __repr__(self):
        return str(self.list_players)