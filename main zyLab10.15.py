# Luis Arroyo
# PSID: 2037081
# CIS 2348

class Team:
    def __init__(self): #Given on zybooks
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self): #Given on zybooks
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":
    team = Team()

    teamname = input()
    wins = int(input())
    losses = int(input())

    team.team_name = teamname
    team.team_wins = wins
    team.team_losses = losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')