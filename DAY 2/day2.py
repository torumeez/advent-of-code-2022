X = [l.strip() for l in open('input2.txt')]
part1 = 0
part2 = 0
for x in X:
    op,me = x.split()
    part1 += {'X': 1, 'Y': 2, 'Z': 3}[me]
    part1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
            }[(op, me)]

    part2 += {'X': 0, 'Y': 3, 'Z': 6}[me]
    part2 += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
            }[(op, me)]
print(part1)
print(part2)