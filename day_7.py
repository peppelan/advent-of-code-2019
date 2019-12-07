import time
import itertools
import queue
from threading import Thread

def computer(memory, input, output, done):
    program = []

    # Parse input
    for op in memory.split(","):
        program.append(int(op))

    # order: 0-based
    def argument(instrNum, argNum):
        modes = program[instrNum] // 100
        mode = (modes // (10 ** argNum)) % 10
        if mode == 1:  # Immediate mode
            return program[instrNum + argNum + 1]
        elif mode == 0:  # Position mode
            position = program[instrNum + argNum + 1]
            return program[position]

    i = 0
    while i < len(program):
        # print("Executing ", i)
        op = program[i] % 100
        # time.sleep(1)

        if op == 99:  # Break
            done.put(True)
            break

        elif op == 1:  # Add
            o1 = argument(i, 0)
            o2 = argument(i, 1)
            destPos = program[i + 3]
            program[destPos] = o1 + o2
            i = i + 4

        elif op == 2:  # Multiply
            o1 = argument(i, 0)
            o2 = argument(i, 1)
            destPos = program[i + 3]
            program[destPos] = o1 * o2
            i = i + 4

        elif op == 3:  # Input
            destPos = program[i + 1]
            value = int(input.get())
            print("Input value:", value)
            program[destPos] = value
            i = i + 2

        elif op == 4:  # Output
            value = argument(i, 0)
            print("Output value:", value)
            output.put(value)
            i = i + 2

        elif op == 5:  # Jump if true
            value = argument(i, 0)
            destPos = argument(i, 1)
            if value != 0:
                i = destPos
            else:
                i = i + 3

        elif op == 6:  # Jump if false
            value = argument(i, 0)
            if value == 0:
                i = argument(i, 1)
            else:
                i = i + 3

        elif op == 7:  # Less-than
            destPos = program[i + 3]
            if argument(i, 0) < argument(i, 1):
                program[destPos] = 1
            else:
                program[destPos] = 0
            i = i + 4

        elif op == 8:  # Equals
            destPos = program[i + 3]
            if argument(i, 0) == argument(i, 1):
                program[destPos] = 1
            else:
                program[destPos] = 0
            i = i + 4

        else:
            print("Non-recognized instruction ", op, " at position ", i)
            print(program)
            break


memory = "3,8,1001,8,10,8,105,1,0,0,21,46,59,84,93,110,191,272,353,434,99999,3,9,101,2,9,9,102,3,9,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99"

phaseSettings = list(itertools.permutations([5,6,7,8,9]))

maxRet = 0

for i in range(len(phaseSettings)):
    inq1 = queue.Queue()
    outq1 = queue.Queue()
    outq2 = queue.Queue()
    outq3 = queue.Queue()
    outq4 = queue.Queue()
    # outq5 = queue.Queue()
    done = queue.Queue()

    inq1.put(phaseSettings[i][0])
    inq1.put(0)
    outq1.put(phaseSettings[i][1])
    outq2.put(phaseSettings[i][2])
    outq3.put(phaseSettings[i][3])
    outq4.put(phaseSettings[i][4])

    Thread(target=computer, args=[memory, inq1, outq1, done]).start()
    Thread(target=computer, args=[memory, outq1, outq2, done]).start()
    Thread(target=computer, args=[memory, outq2, outq3, done]).start()
    Thread(target=computer, args=[memory, outq3, outq4, done]).start()
    Thread(target=computer, args=[memory, outq4, inq1, done]).start()

    for i in range(5):
        done.get()

    ret = inq1.get()
    if ret > maxRet:
        maxRet = ret

print("Final output", maxRet)
