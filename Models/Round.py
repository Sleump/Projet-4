from datetime import datetime

#begin_time:datetime, #end_time:datetime):

class Round:
    def __init__(self, matchs, name, begin_time, end_time):
        self.matchs = matchs    # liste => matchs_first_round , matchs_second_round
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time

    def __repr__(self):
        return str(self.matchs)

    def __str__(self):
        return str(self.matchs)
