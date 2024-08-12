def get_longest_pass_player(stats):
    longest_pass = max(stats.items(), key=lambda x: x[1]["max_distance"])
    long_distance_value = longest_pass[1]["max_distance"]
    player = longest_pass[0]
    player_long_distance = {player: long_distance_value}
   
    return player_long_distance