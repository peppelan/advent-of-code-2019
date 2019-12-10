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

reachabilityMap = [[len(asteroids) - 1 for j in range(cols)] for i in range(rows)]

# compute the shadow made by a2 on the light shed by a1
for i in range(len(asteroids)):
    for j in range(len(asteroids)):
        if i == j:
            continue

        a1 = asteroids[i]
        a2 = asteroids[j]

        delta = (a2[0] - a1[0], a2[1] - a1[1])

        # find reduced delta
        reducedDelta = delta
        for mcd in range(1, min(abs(delta[0]), abs(delta[1])) + 1):
            if delta[0]//mcd == delta[0]/mcd and delta[1]//mcd == delta[1]/mcd:
                reducedDelta = (delta[0]//mcd, delta[1]//mcd)

        k = 1
        while True:
            thisDelta = (reducedDelta[0] * k, reducedDelta[1] * k)
            thisPos = (a2[0] + thisDelta[0], a2[1] + thisDelta[1])
            # print(delta, reducedDelta, k, thisDelta, thisPos)
            if thisPos[0] >= rows or thisPos[0] < 0 or thisPos[1] >= cols or thisPos[1] < 0:
                break

            reachabilityMap[thisPos[0]][thisPos[1]] -= 1

            k += 1

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
