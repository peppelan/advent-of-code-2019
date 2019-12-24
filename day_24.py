input = """.##.#
###..
#...#
##.#.
.###."""

maze = []

for line in input.split('\n'):
    maze.append([])

    for c in line:
        maze[-1].append(c == '#')

rows = len(maze)
cols = len(maze[0])

biodiversity = 0
for i in range(rows):
    for j in range(cols):
        if maze[i][j]:
            biodiversity += 2 ** ((i * cols) + j)
maze = biodiversity

def get(biodiversity, i, j):
    return (biodiversity & int(2 ** ((i*cols) + j))) != 0

def toggle(biodiversity, i, j):
    return biodiversity ^ int(2 ** ((i*cols) + j))

maze = {i: 0 for i in range(-200, 200)}
maze[0] = biodiversity

for w in range(200):
    # evolve
    mutations = set()

    for k in range(-200, 200):
        biodiversity = maze[k]
        for i in range(rows):
            for j in range(cols):
                if (i, j) == (2, 2):
                    continue

                potentialNeighs = []

                for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ni = i + dir[0]
                    nj = j + dir[1]

                    if ni < 0:
                        potentialNeighs.append((k - 1, 1, 2))
                    elif ni == rows:
                        potentialNeighs.append((k - 1, 3, 2))
                    elif nj < 0:
                        potentialNeighs.append((k - 1, 2, 1))
                    elif nj == cols:
                        potentialNeighs.append((k - 1, 2, 3))
                    elif (ni, nj) == (2, 2):
                        if (i, j) == (1, 2):
                            potentialNeighs.append((k + 1, 0, 0))
                            potentialNeighs.append((k + 1, 0, 1))
                            potentialNeighs.append((k + 1, 0, 2))
                            potentialNeighs.append((k + 1, 0, 3))
                            potentialNeighs.append((k + 1, 0, 4))
                        elif (i, j) == (3, 2):
                            potentialNeighs.append((k + 1, 4, 0))
                            potentialNeighs.append((k + 1, 4, 1))
                            potentialNeighs.append((k + 1, 4, 2))
                            potentialNeighs.append((k + 1, 4, 3))
                            potentialNeighs.append((k + 1, 4, 4))
                        elif (i, j) == (2, 1):
                            potentialNeighs.append((k + 1, 0, 0))
                            potentialNeighs.append((k + 1, 1, 0))
                            potentialNeighs.append((k + 1, 2, 0))
                            potentialNeighs.append((k + 1, 3, 0))
                            potentialNeighs.append((k + 1, 4, 0))
                        else: # 2, 3
                            potentialNeighs.append((k + 1, 0, 4))
                            potentialNeighs.append((k + 1, 1, 4))
                            potentialNeighs.append((k + 1, 2, 4))
                            potentialNeighs.append((k + 1, 3, 4))
                            potentialNeighs.append((k + 1, 4, 4))
                    else:
                        potentialNeighs.append((k, ni, nj))

                neighs = 0

                for nk, ni, nj in potentialNeighs:
                    if nk not in maze:
                        continue

                    if get(maze[nk], ni, nj):
                        neighs += 1

                        # print(k, i, j, "has", nk, ni, nj, "as infested neighbor")


                if get(biodiversity, i, j):
                    if neighs != 1:
                        mutations.add((k,i,j))
                else:
                    if neighs == 1 or neighs == 2:
                        mutations.add((k,i,j))

    for k,i,j in mutations:
        maze[k] = toggle(maze[k], i, j)

bugs = 0
for k in range(-200, 200):
    biodiversity = maze[k]

    for i in range(rows):
        for j in range(cols):
            if get(biodiversity, i, j):
                bugs += 1

print(bugs)