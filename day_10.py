import math

input = """#.#.##..#.###...##.#....##....###
...#..#.#.##.....#..##.#...###..#
####...#..#.##...#.##..####..#.#.
..#.#..#...#..####.##....#..####.
....##...#.##...#.#.#...#.#..##..
.#....#.##.#.##......#..#..#..#..
.#.......#.....#.....#...###.....
#.#.#.##..#.#...###.#.###....#..#
#.#..........##..###.......#...##
#.#.........##...##.#.##..####..#
###.#..#####...#..#.#...#..#.#...
.##.#.##.........####.#.#...##...
..##...#..###.....#.#...#.#..#.##
.#...#.....#....##...##...###...#
###...#..#....#............#.....
.#####.#......#.......#.#.##..#.#
#.#......#.#.#.#.......##..##..##
.#.##...##..#..##...##...##.....#
#.#...#.#.#.#.#..#...#...##...#.#
##.#..#....#..##.#.#....#.##...##
...###.#.#.......#.#..#..#...#.##
.....##......#.....#..###.....##.
........##..#.#........##.......#
#.##.##...##..###.#....#....###.#
..##.##....##.#..#.##..#.....#...
.#.#....##..###.#...##.#.#.#..#..
..#..##.##.#.##....#...#.........
#...#.#.#....#.......#.#...#..#.#
...###.##.#...#..#...##...##....#
...#..#.#.#..#####...#.#...####.#
##.#...#..##..#..###.#..........#
..........#..##..#..###...#..#...
.#.##...#....##.....#.#...##...##"""

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
    foundAngles = set()
    a1 = asteroids[i]

    for j in range(len(asteroids)):
        if i == j:
            continue

        a2 = asteroids[j]

        delta = (a2[0] - a1[0], a2[1] - a1[1])

        angle = math.atan2(delta[0], delta[1])

        if angle not in foundAngles:
            reachabilityMap[a1[0]][a1[1]] += 1
            foundAngles.add(angle)


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

station = minimum

#print(asteroids)
#print(station)

angles = []
knownAngles = set()
angleToAsteroids = {}


for asteroid in asteroids:
    delta = (asteroid[0] - station[0], asteroid[1] - station[1])
    angle = math.atan2(delta[0], delta[1]) + math.pi/2

    # print(station, asteroid, delta, angle)

    if angle not in knownAngles:
        angles.append(angle)
        knownAngles.add(angle)
        angleToAsteroids[angle] = []

    angleToAsteroids[angle].append(asteroid)

angles = sorted(angles)
#print(angles)
firstAngleIdx = None

# find first angle:
for angleIdx in range(len(angles)):
    angle = angles[angleIdx]
    if angle >= 0 and (firstAngleIdx is None or angle < angles[firstAngleIdx]):
        firstAngleIdx = angleIdx

# print(firstAngleIdx, angles[firstAngleIdx])


for angle in angles:
    asteroidsAtAngle = angleToAsteroids[angle]
    angleToAsteroids[angle] = sorted(angleToAsteroids[angle], key=lambda x: (x[0] - station[0])**2 + (x[1] - station[1])**2)

print(angleToAsteroids)

destroyed = []
angleIdx = firstAngleIdx
while len(angleToAsteroids) > 0:
    if angles[angleIdx] in angleToAsteroids:
        asteroidsAtAngle = angleToAsteroids[angles[angleIdx]]

        asteroid = asteroidsAtAngle.pop(0)
        destroyed.append(asteroid)

        print("Removing ", asteroid, " at angle ", angles[angleIdx])

        if len(asteroidsAtAngle) == 0:
            angleToAsteroids.pop(angles[angleIdx])


    # increase the angle
    angleIdx += 1
    if angleIdx == len(angles):
        angleIdx = 0

print(destroyed[0])
print(destroyed[1])
print(destroyed[2])
print(destroyed[9])
print(destroyed[19])
print(destroyed[49])
print(destroyed[99])
print(destroyed[198])
print(destroyed[199])
print(destroyed[200])
print(destroyed[-1])

bet = destroyed[199]

print(bet[1]*100+bet[0])
