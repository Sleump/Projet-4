class Player:
    def __init__(self, name, firstname, birth, gender, rank, score = 0):
        self.name = name         #player_name
        self.firstname = firstname  #player_firstname
        self.birth = birth   #player_birth
        self.gender = gender  #player_gender
        self.rank = rank      #player_rank
        self.score = 0    #player_score
        self.username = self.firstname +' '+ self.name

    def points(self, points):
        self.score += points

    def __repr__(self):
        return f"{self.firstname}"





