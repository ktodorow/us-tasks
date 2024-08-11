from collections import defaultdict
from player_stats import MostCompletePlayer, LongestPassPlayer

# data
passes = [
    {"result": "incomplete", "receiver": "Demaryius Thomas", "distance": 0.7},
    {"result": "complete", "receiver": "Tim Patrick", "distance": 0.9},
    {"result": "complete", "receiver": "Demaryius Thomas", "distance": 0.3},
    {"result": "incomplete", "receiver": "Tim Patrick", "distance": 0.9},
    {"result": "incomplete", "receiver": "Tim Patrick", "distance": 0.8},
    {"result": "complete", "receiver": "Demaryius Thomas", "distance": 0.1},
    {"result": "interception", "receiver": "Demaryius Thomas", "distance": 0.4},
]

receiver_stats = defaultdict(lambda: {"complete": 0, "total": 0, "max_distance": 0})

for p in passes:
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