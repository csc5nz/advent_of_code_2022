"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

14470
"""

with open("input.txt") as f:
    lines = f.readlines()

shape_points = {"A": 1, "B": 2, "C": 3}
lose = {"A": "C", "B": "A", "C": "B"}
win = {"A": "B", "B": "C", "C": "A"}
score = 0

for line in lines:
    shape, move = line[0], line[2]
    if move == "X": #lose
        score += shape_points[lose[shape]]
        score += 0
    elif move == "Y": # draw
        score += shape_points[shape]
        score += 3
    else: # win
        score += shape_points[win[shape]]
        score += 6

print("score: ", score)
