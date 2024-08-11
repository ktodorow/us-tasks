from collections import defaultdict
from most_complete_operation import get_most_complete_player
from longest_pass_operation import get_longest_pass_player

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

most_complete_player = next(iter(get_most_complete_player(receiver_stats).items()))
longest_pass_player = next(iter(get_longest_pass_player(receiver_stats).items()))

most_complete_percentage = {
    "player": most_complete_player[0],
    "value": f"{most_complete_player[1]:.2f}%"
}

long_distance_pass = {
    "player": longest_pass_player[0],
    "value": f"{longest_pass_player[1]:.1f}"
}

print("Most Complete Percentage:", most_complete_percentage)
print("Longest Distance Pass:", long_distance_pass)