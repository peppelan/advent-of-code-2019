import queue
from threading import Thread

def computer(memory, input, output, done):
    program = []

    # Parse input
    for op in memory.split(","):
        program.append(int(op))

    def initPosition(position):
        for i in range(len(program), position + 1):
            program.append(0)

    # order: 0-based
    def argument(instrNum, argNum, isDest):
        modes = program[instrNum] // 100
        mode = (modes // (10 ** argNum)) % 10

        if mode == 1:  # Immediate mode
            position = instrNum + argNum + 1
        elif mode == 0:  # Position mode
            position = program[instrNum + argNum + 1]
        elif mode == 2:  # Relative mode
            position = relativeBase + program[instrNum + argNum + 1]

        initPosition(position)

        if isDest:
            return position
        else:
            return program[position]

    i = 0
    relativeBase = 0

    while i < len(program):

        op = program[i] % 100
        # time.sleep(1)
        #print("Executing ", i, op)

        if op == 99:  # Break
            done.put(True)
            break

        elif op == 1:  # Add
            o1 = argument(i, 0, False)
            o2 = argument(i, 1, False)
            destPos = argument(i, 2, True)
            program[destPos] = o1 + o2
            i = i + 4

        elif op == 2:  # Multiply
            o1 = argument(i, 0, False)
            o2 = argument(i, 1, False)
            destPos = argument(i, 2, True)
            program[destPos] = o1 * o2
            i = i + 4

        elif op == 3:  # Input
            destPos = argument(i, 0, True)
            value = int(input.get())
            # print("Input value:", value)
            program[destPos] = value
            i = i + 2

        elif op == 4:  # Output
            value = argument(i, 0, False)
            # print("Output value:", value)
            output.put(value)
            i = i + 2

        elif op == 5:  # Jump if true
            value = argument(i, 0, False)
            destPos = argument(i, 1, False)
            if value != 0:
                i = destPos
            else:
                i = i + 3

        elif op == 6:  # Jump if false
            value = argument(i, 0, False)
            if value == 0:
                i = argument(i, 1, False)
            else:
                i = i + 3

        elif op == 7:  # Less-than
            destPos = argument(i, 2, True)
            if argument(i, 0, False) < argument(i, 1, False):
                program[destPos] = 1
            else:
                program[destPos] = 0
            i = i + 4

        elif op == 8:  # Equals
            destPos = argument(i, 2, True)
            if argument(i, 0, False) == argument(i, 1, False):
                program[destPos] = 1
            else:
                program[destPos] = 0
            i = i + 4

        elif op == 9:  # Adjust relative base
            value = argument(i, 0, False)
            relativeBase += value
            i = i + 2
            #print("Relative base:", relativeBase)

        else:
            print("Non-recognized instruction ", op, " at position ", i)
            print(program)
            break


memory = "3,8,1005,8,321,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,29,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,50,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,73,1,1105,16,10,2,1004,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,103,1006,0,18,1,105,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,131,1006,0,85,1,1008,0,10,1006,0,55,2,104,4,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,168,2,1101,1,10,1006,0,14,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,196,1006,0,87,1006,0,9,1,102,20,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,228,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,250,2,5,0,10,2,1009,9,10,2,107,17,10,1006,0,42,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,287,2,102,8,10,1006,0,73,1006,0,88,1006,0,21,101,1,9,9,1007,9,925,10,1005,10,15,99,109,643,104,0,104,1,21102,1,387353256856,1,21101,0,338,0,1105,1,442,21101,936332866452,0,1,21101,349,0,0,1105,1,442,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,179357024347,1,21101,0,396,0,1105,1,442,21102,1,29166144659,1,21102,407,1,0,1105,1,442,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,718170641252,1,21102,430,1,0,1106,0,442,21101,825012151040,0,1,21102,441,1,0,1106,0,442,99,109,2,21202,-1,1,1,21102,1,40,2,21102,1,473,3,21102,463,1,0,1105,1,506,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,468,469,484,4,0,1001,468,1,468,108,4,468,10,1006,10,500,1102,1,0,468,109,-2,2105,1,0,0,109,4,1202,-1,1,505,1207,-3,0,10,1006,10,523,21101,0,0,-3,22101,0,-3,1,21202,-2,1,2,21102,1,1,3,21102,1,542,0,1105,1,547,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,570,2207,-4,-2,10,1006,10,570,22102,1,-4,-4,1105,1,638,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,589,0,1106,0,547,22102,1,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,608,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,630,21202,-1,1,1,21102,630,1,0,105,1,505,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"
out = queue.Queue()
done = queue.Queue()
input = queue.Queue()
# input.put(0)

turnLeft = {
    (-1,  0) : ( 0, -1), # up    -> left
    ( 0, -1) : ( 1,  0), # left  -> down
    ( 1,  0) : ( 0,  1), # down  -> right
    ( 0,  1) : (-1,  0)  # right -> up
}

turnRight = {
    ( 0, -1) : (-1,  0), # left  -> up
    ( 1,  0) : ( 0, -1), # down  -> left
    ( 0,  1) : ( 1,  0), # right -> down
    (-1,  0) : ( 0,  1)  # up    -> right
}

Thread(target=computer, args=[memory, input, out, done]).start()

# initial values

whitePositions = set()
paintedPositions = set()
whitePositions.add((0,0))

def feed():
    direction = (-1, 0)
    position = (0, 0)

    while done.empty():
        if position in whitePositions:
            input.put(1)
        else:
            input.put(0)

        if out.get() == 0:
            if position in whitePositions:
                whitePositions.remove(position)
            #print("Painting black ", position)
        else:
            #print("Painting white ", position)
            whitePositions.add(position)

        #if position in paintedPositions:
            #print("Painting again ", position)

        paintedPositions.add(position)
        print("Painted ", len(paintedPositions))

        if out.get() == 0:
            direction = turnLeft[direction]
        else:
            direction = turnRight[direction]

        #print("Heading ", direction)

        position = (position[0] + direction[0], position[1] + direction[1])


Thread(target=feed).start()

done.get()

minRow = 1000
maxRow = -1000
minCol = 1000
maxCol = -1000

for row, col in whitePositions:
    if row < minRow:
        minRow = row

    if col < minCol:
        minCol = col

    if row > maxRow:
        maxRow = row

    if col > maxCol:
        maxCol = col

print(minRow, maxRow, minCol, maxCol)

rows = maxRow - minRow + 1
cols = maxCol - minCol + 1

print(rows, cols)

for i in range(minRow, maxRow+1):
    for j in range(minCol, maxCol+1):
        if (i,j) in whitePositions:
            print("#", end='')
        else:
            print(" ", end='')
    print()
