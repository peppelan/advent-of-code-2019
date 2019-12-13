moons = [
    [4, 1, 1, 0, 0, 0],
    [11, -18, -1, 0, 0, 0],
    [-2, -10, -4, 0, 0, 0],
    [-7, -2, 14, 0, 0, 0],
]


for moon in moons:
    print(moon)

print()

previousEnergy = 0

for i in range(1000):

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

    energy = 0
    thisRound = 0

    for moon in moons:
        potential = 0
        kinetic = 0

        for w in [0,1,2]:
            potential += abs(moon[w])
            kinetic += abs(moon[w+3])

        thisRound += potential * kinetic

    print(thisRound)
    energy += thisRound


# for moon in moons:
#     print(moon)
#
