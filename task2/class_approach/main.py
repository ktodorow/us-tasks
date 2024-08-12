import json
from collections import defaultdict
from player_stats import MostCompletePlayer, LongestPassPlayer

with open('passes.json', 'r') as file:
    data = json.load(file)

receiver_stats = defaultdict(lambda: {"complete": 0, "total": 0, "max_distance": 0})

for p in data:
    receiver = p["receiver"]
    result = p["result"]
    distance = p["distance"]

    if result == "complete":
        receiver_stats[receiver]["complete"] += 1
    receiver_stats[receiver]["total"] += 1
    if distance > receiver_stats[receiver]["max_distance"]:
        receiver_stats[receiver]["max_distance"] = distance

most_complete_calculator = MostCompletePlayer(receiver_stats)
longest_pass_calculator = LongestPassPlayer(receiver_stats)

most_complete_percentage = most_complete_calculator.get_player()
long_distance_pass = longest_pass_calculator.get_player()

print("Most Complete Percentage:", most_complete_percentage)
print("Longest Distance Pass:", long_distance_pass)