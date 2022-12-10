
"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

787 low

"""

with open("input.txt") as f:
    lines = f.readlines()

count = 0
for line in lines:
    elf1, elf2 = line[:-1].split(',')
    elf1 = elf1.split('-')
    elf2 = elf2.split('-')

    e1_subgroup = int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])
    e2_subgroup = int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])    
    intersect1 = int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[0])
    intersect2 = int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[1])
    
    if intersect1 or intersect2 or e1_subgroup or e2_subgroup:
        count += 1

print("count: ", count)