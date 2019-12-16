input = "59776034095811644545367793179989602140948714406234694972894485066523525742503986771912019032922788494900655855458086979764617375580802558963587025784918882219610831940992399201782385674223284411499237619800193879768668210162176394607502218602633153772062973149533650562554942574593878073238232563649673858167635378695190356159796342204759393156294658366279922734213385144895116649768185966866202413314939692174223210484933678866478944104978890019728562001417746656699281992028356004888860103805472866615243544781377748654471750560830099048747570925902575765054898899512303917159138097375338444610809891667094051108359134017128028174230720398965960712"

basePattern = [0, 1, 0, -1]



def preparePattern(basePattern, position, maxLen):
    res = []

    i = 0
    while len(res) < maxLen + 1:
        res.append(basePattern[(i//position) % len(basePattern)])
        i+=1

    return res[1:]

patterns = [preparePattern(basePattern, i+1, len(input)) for i in range(len(input))]
print(patterns)

def shiftPattern(a, position, c):
    return patterns[position -1]

def apply(signal, basePattern):
    output = []
    for i in range(len(signal)):
    # for i in range(2):
        result = 0
        pattern = shiftPattern(basePattern, i+1, len(signal))
        for j in range(len(signal)):
            # print(int(signal[j]), "*", pattern[j%len(pattern)])
            result += int(signal[j]) * pattern[j%len(pattern)]

        output.append(abs(result)%10)
    return output

o = input

for i in range(100):
    o = apply(o, basePattern)

print("".join(str(o[:8])))