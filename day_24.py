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

biodiversities = set()


while True:
    # evolve
    mutations = set()

    for i in range(rows):
        for j in range(cols):
            neighs = 0
            for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni = i + dir[0]
                nj = j + dir[1]

                if 0 <= ni < rows and 0 <= nj < cols and get(biodiversity, ni, nj):
                    neighs += 1

            if get(biodiversity, i, j):
                if neighs != 1:
                    mutations.add((i,j))
            else:
                if neighs == 1 or neighs == 2:
                    mutations.add((i,j))

    for i,j in mutations:
        biodiversity = toggle(biodiversity, i, j)
        # print("mutating", i, j)

    # for i in range(rows):
    #     for j in range(cols):
    #         if get(biodiversity, i, j):
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print()

    if biodiversity in biodiversities:
        print(biodiversity)
        break
    else:
        biodiversities.add(biodiversity)