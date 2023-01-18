class Player:
    def __init__(self, name, firstname, birth, gender, rank, score):
        self.name = name
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.rank = rank
        self.score = score
        self.username = self.firstname +' '+ self.name


    def update_score(self, points):
        self.score = self.score + points

    def __repr__(self):
        return self.username





