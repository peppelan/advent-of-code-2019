import math

input = """.#..#
.....
#####
....#
...##"""

asteroidsBoard = []
for line in input.split():
    row = []
    for char in line:
        if char == "#":
            row.append(True)
        else:
            row.append(False)

    asteroidsBoard.append(row)


rows = len(asteroidsBoard)
cols = len(asteroidsBoard[0])
asteroids = []
for i in range(rows):
    for j in range(cols):
        if asteroidsBoard[i][j]:
            asteroids.append((i, j))

# print(asteroids)

reachabilityMap = [[0 for j in range(cols)] for i in range(rows)]

# compute if a2 is visible from a1 (there is no a3 in the middle with the same angle)
for i in range(len(asteroids)):
    for j in range(len(asteroids)):
        if i == j:
            continue

        a1, a2 = asteroids[i], asteroids[j]

        visible = True
        delta = (a2[0] - a1[0], a2[1] - a1[1])

        angle = math.atan2(delta[0], delta[1])
        distance = delta[0] ** 2 + delta[1] ** 2

        for k in range(len(asteroids)):
            if k == i or k == j:
                continue

            a3 = asteroids[k]
            delta2 = (a3[0] - a1[0], a3[1] - a1[1])
            angle2 = math.atan2(delta2[0], delta2[1])
            distance2 = delta2[0] ** 2 + delta2[1] ** 2

            if angle2 == angle and distance2 < distance:
                visible = False
                break

        if visible:
            reachabilityMap[a1[0]][a1[1]] += 1


minimum = None

for i in range(rows):
    for j in range(cols):
        if not asteroidsBoard[i][j]:
            continue
        if minimum is None or (reachabilityMap[i][j] > reachabilityMap[minimum[0]][minimum[1]]):
            minimum = (i,j)

for line in reachabilityMap:
    print("".join([str(c) + " " for c in line]))

print(minimum)
print(reachabilityMap[minimum[0]][minimum[1]])
