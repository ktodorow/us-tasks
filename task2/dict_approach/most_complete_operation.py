def get_most_complete_player(stats):
    most_complete = max(stats.items(), key=lambda x: x[1]["complete"] / x[1]["total"])
    complete_percentage = (most_complete[1]["complete"] / most_complete[1]["total"]) * 100
    player = most_complete[0]
    player_most_complete = {player: complete_percentage}
    
    return player_most_complete