import math
import functools

moons = [
    [4, 1, 1, 0, 0, 0],
    [11, -18, -1, 0, 0, 0],
    [-2, -10, -4, 0, 0, 0],
    [-7, -2, 14, 0, 0, 0],
]


# moons = [
#    [ -1,  0,  2, 0, 0, 0 ],
#    [  2,-10, -7, 0, 0, 0 ],
#    [  4, -8,  8, 0, 0, 0 ],
#    [  3,  5, -1, 0, 0, 0 ],
# ]




for moon in moons:
    print(moon)

print()

previousEnergy = 0

i = 0
# Find the cycle of each axis, then return the mcm
cycles = {}
combinations = {0:set(), 1:set(), 2:set()}

while True:

    # gravity:
    # moon1
    for j in range(len(moons)):
        # moon2
        for k in range(j+1, len(moons)):
            m1, m2 = moons[j], moons[k]

            # coordinate
            for w in [0, 1, 2]:
                if m1[w] == m2[w]:
                    continue
                elif m1[w] < m2[w]:
                    m1[w+3] += 1
                    m2[w+3] -= 1
                else:
                    m1[w+3] -= 1
                    m2[w+3] += 1

    # velocity
    for moon in moons:
        for w in [0, 1, 2]:
            moon[w] += moon[w+3]

    for w in range(3):
        if w in cycles:
            continue

        combination = tuple([tuple([moons[m][w] for m in range(len(moons))]),
                             tuple([moons[m][w + 3] for m in range(len(moons))])])

        if combination in combinations[w]:
            cycles[w] = i
        else:
            combinations[w].add(combination)

    if len(cycles) == 3:
        break


    i += 1


print(cycles)#

a = list(cycles.values())
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i//math.gcd(lcm, i)
print(lcm)

# for moon in moons:
#     print(moon)
#
