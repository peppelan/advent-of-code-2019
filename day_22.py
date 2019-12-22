totalCards = 10007
# deck = {x: x for x in range(totalCards)}

input = """deal into new stack
deal with increment 21
cut -1639
deal with increment 32
cut -873
deal with increment 8
deal into new stack
cut -7730
deal with increment 8
cut -8408
deal with increment 42
cut -4951
deal into new stack
deal with increment 24
cut -6185
deal with increment 69
cut -930
deal into new stack
cut 8675
deal with increment 47
cut -4543
deal with increment 62
deal into new stack
deal with increment 23
cut 7128
deal with increment 29
deal into new stack
deal with increment 65
cut 8232
deal with increment 34
deal into new stack
deal with increment 7
deal into new stack
cut -5590
deal with increment 34
cut -3523
deal with increment 24
cut 8446
deal with increment 42
cut 6714
deal into new stack
deal with increment 60
cut 1977
deal with increment 51
cut 2719
deal with increment 45
cut 9563
deal with increment 33
cut 9036
deal with increment 70
cut 3372
deal with increment 60
cut 9686
deal with increment 7
cut 9344
deal with increment 13
cut 797
deal with increment 12
cut -6989
deal with increment 43
deal into new stack
cut 1031
deal with increment 14
cut -1145
deal with increment 26
cut -9008
deal with increment 14
cut 432
deal with increment 46
cut -65
deal with increment 50
cut -704
deal with increment 4
cut 7372
deal with increment 66
cut 690
deal with increment 60
cut -7137
deal with increment 66
cut 9776
deal with increment 30
cut 3532
deal with increment 62
cut 4768
deal with increment 13
deal into new stack
cut -9014
deal with increment 68
cut -9601
deal with increment 6
cut -7535
deal with increment 74
cut 9479
deal with increment 6
cut -1879
deal with increment 33
cut 3675
deal with increment 19
cut -937
deal with increment 42"""

position = 2019

seen = {position}

for i in range(1):
    if i != 0 and position in seen:
        print(i)
        break
    else:
        seen.add(position)

    for action in input.split('\n'):
        # print('.', end='')
        if "deal with increment" in action:
            increment = int(action[20:])
            position *= increment
        elif "deal into new stack" in action:
            position *= -1
            position -= 1
        elif "cut" in action:
            cut = int(action[4:])
            position -= cut

print(position%totalCards)