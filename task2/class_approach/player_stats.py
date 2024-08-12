class PlayerStats:
    def __init__(self, stats):
        self.stats = stats

    def get_player(self):
        raise NotImplementedError("Subclasses should implement this method.")

class LongestPassPlayer(PlayerStats):
    def get_player(self):
        longest_pass = max(self.stats.items(), key=lambda x: x[1]["max_distance"])
        long_distance_value = longest_pass[1]["max_distance"]
        player = longest_pass[0]
        return {"player": player, "value": f"{long_distance_value:.1f}"}

class MostCompletePlayer(PlayerStats):
    def get_player(self):
        most_complete = max(self.stats.items(), key=lambda x: x[1]["complete"] / x[1]["total"])
        complete_percentage = (most_complete[1]["complete"] / most_complete[1]["total"]) * 100
        player = most_complete[0]
        return {"player": player, "value": f"{complete_percentage:.0f}%"}
