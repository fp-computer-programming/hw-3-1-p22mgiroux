# Author: MOG 9/28/21

team1_wins = input("How many wins did team 1 have? ")
team1_ties = input("How many ties did team 1 have? ")
team2_wins = input("How many wins did team 2 have? ")
team2_ties = input("How many ties did team 2 have? ")
team1_pts = (int(team1_wins) * 3) + (int(team1_ties))
team2_pts = (int(team2_wins) * 3) + (int(team2_ties))

if team1_pts == team2_pts:
    print("The teams tied with " + str(team1_pts) + " points!")
else: 
    if team1_pts > team2_pts:
        print("Team 1 Wins with " + str(team1_pts) + " points!")
    else:
        print("Team 2 Wins with " + str(team2_pts) + " points!")