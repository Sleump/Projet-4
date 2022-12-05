
"""Base view."""

class ViewTournament:
    """Tournament view."""

    def prompt_for_tournament_name(self):
        """Prompt for a name."""
        tournament_name = input("Tapez le nom du tournoi : ")
        if not tournament_name:
            return None
        return tournament_name

    def prompt_for_place(self):
        """Prompt for a place."""
        place = input("Tapez le nom du lieu du tournoi : ")
        if not place:
            return None
        return place

    def prompt_for_day(self):
        """Prompt for a day."""
        day = input("Tapez la date du tournoi : ")
        if not day:
            return None
        return day

    def prompt_for_players(self):
        """Prompt for players."""
        players = input("Tapez le nombre de joueurs ")
        if not players:
            return None
        return players

    def prompt_for_description(self):
        """Prompt for description."""
        description = input("Décrivez le Tournoi ")
        if not description:
            return None
        return description

    def prompt_for_time_control(self):
        """Prompt for timecontrol."""
        time_control = input("Indiquez le temps en secondes de chaque tour de joueur ")
        if not time_control:
            return None
        return time_control

    def prompt_for_turns(self,):
        """ faire une fonction pour tournoi pour + de visibilité et non plusieurs prompt => Promp to create a tournament"""
        pass

class ViewPlayer:
    """Player view."""

    def prompt_for_player_name(self):
        """Prompt for a player's name."""
        player_name = input("Tapez le nom du joueur : ")
        if not player_name:
            return None
        return player_name

    def prompt_for_player_firstname(self):
        """Prompt for a player's firstname."""
        player_firstname = input("Tapez le prénom du joueur : ")
        if not player_firstname:
            return None
        return player_firstname

    def prompt_for_player_birth(self):
        """Prompt for a player's birth."""
        player_birth = input("Tapez la date de naissance du joueur : ")
        if not player_birth:
            return None
        return player_birth

    def prompt_for_player_gender(self):
        """Prompt for a player's gender."""
        player_gender = input("Tapez le sexe du joueur : ")
        if not player_gender:
            return None
        return player_gender

    def prompt_for_player_rank(self):
        """Prompt for a player's ladder."""
        player_rank = input("Tapez le rang du joueur : ")
        if not player_rank:
            return None
        return player_rank



class ViewMatch:

    def prompt_for_player_result(self, list_players):
        """Prompt for a winner name."""                      #([player1, score], [player2, score])
        new_list = []
        for player in list_players:
            result_match_player_one = float(input("Tapez le score du  joueur  soit 0 , 1 ou 0.5: " ))
            player[0].score += result_match_player_one
            #player[0].update_score(result_match_player_one)
            new_list.append([player[0], player[0].score])
        return new_list



class Round:

    def prompt_for_begin_time(self):
        begin = input("Tapez l'heure de début du tour:")

    def prompt_for_end_time(self):
        end = input("Tapez l'heure de fin du tour:")
