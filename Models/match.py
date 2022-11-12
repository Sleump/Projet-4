class Match:
    def __init__(self, player1, player2, name):
        self.list_players = ([player1, 0], [player2, 0])  #     0 => score joueur initialisé au début
        self.name = name

    def __repr__(self):
        return str(self.list_players)