import queue
from threading import Thread
import collections

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


memory = "109,424,203,1,21102,11,1,0,1106,0,282,21101,18,0,0,1106,0,259,2101,0,1,221,203,1,21102,31,1,0,1106,0,282,21102,1,38,0,1105,1,259,20102,1,23,2,22101,0,1,3,21101,0,1,1,21101,0,57,0,1106,0,303,1202,1,1,222,21001,221,0,3,20102,1,221,2,21102,259,1,1,21101,80,0,0,1105,1,225,21102,1,149,2,21101,0,91,0,1105,1,303,1202,1,1,223,21002,222,1,4,21102,259,1,3,21102,225,1,2,21102,225,1,1,21101,118,0,0,1105,1,225,20102,1,222,3,21101,0,127,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,1201,1,0,223,21001,221,0,4,21002,222,1,3,21102,14,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,0,-1,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22102,1,-3,1,21201,-2,0,2,21201,-1,0,3,21102,1,250,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21101,343,0,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21102,1,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2106,0,0"
out = queue.Queue()
done = queue.Queue()
input = queue.Queue()

count = 0

for i in range(50):
    for j in range(50):
        input.put(j)
        input.put(i)

        Thread(target=computer, args=[memory, input, out, done]).start()
        done.get()
        value = out.get()

        print(value, end='')
        if value == 1:
            count += 1

    print()

print(count)