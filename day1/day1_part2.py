"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

import heapq

with open('input.txt') as f:
    lines = f.readlines()

running_total = 0
heap = []
for line in lines:
    if line == "\n":
        heapq.heappush(heap, running_total)
        running_total = 0
        continue
    running_total += -1*int(line[:-1])

total = 0
for i in range(3):
    total += -1*heapq.heappop(heap)
print("max calories: ", total)