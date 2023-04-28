# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number  on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# Example



# The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

# Function Description

# Complete the climbingLeaderboard function in the editor below.

# climbingLeaderboard has the following parameter(s):

# int ranked[n]: the leaderboard scores
# int player[m]: the player's scores
# Returns

# int[m]: the player's rank after each new score


def climbingLeaderboard(ranked, player):
    result = []
    ranked = sorted(list(set(ranked)), reverse=True)
    for play in player:
        for i in range(len(ranked)):
           
            if ranked[i] > play and i < len(ranked)-1:
                continue
            else:
                if ranked[i] > play and i == len(ranked)-1:
                    result.append(i+2)
                    break

                result.append(i+1)
                break
    
    return result