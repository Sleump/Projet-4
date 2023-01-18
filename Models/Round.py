from datetime import datetime

#begin_time:datetime, #end_time:datetime):

class Round:
    def __init__(self, name, begin_time, matches, end_time):
        self.name = name
        self.begin_time = begin_time
        self.matches = matches
        self.end_time = end_time

    def __repr__(self):
        return str(self.matches)

    def __str__(self):
        return str(self.matches)
