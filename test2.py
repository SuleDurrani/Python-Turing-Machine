def getState():
    s = [
        [['1', 'Z', 'R', '1', 0], ['0', 'B', 'R', '6', 0]],  # 0
        [['1', '1', 'R', '1', 1], ['0', '0', 'R', '2', 1]],  # 1
        [['0', '0', 'L', '5', 2], ['1', 'Y', 'R', '3', 2]],  # 2
        [['1', '1', 'R', '3', 3], ['0', '0', 'R', '3', 3], ['B', '1', 'L', '4', 3]],  # 3
        [['0', '0', 'L', '4', 4], ['1', '1', 'L', '4', 4], ['Y', 'Y', 'R', '2', 4]],  # 4
        [['Y', '1', 'L', '5', 5], ['1', '1', 'L', '5', 5], ['0', '0', 'L', '5', 5], ['Z', 'Z', 'R', '0', 5]],  # 5
        [['B', '1', 'R', '6', 6], ['B', 'B', 'R', '1000', 6]]]  # 6
    return s


def comparison(tapee):
    state = getState()
    tape = tapee
    current = 10

    x = 0
    e = 0
    leaveLoop = ""
    print("tc=" + str(tape))
    while leaveLoop != "1000":
        print('x= ' + str(x))
        print('e= ' + str(e))

        for e in range(len(state[x])):
            print("e" + str(e))
            if state[x][e][0] == tape[current]:
                w = str(state[x][e][1])
                tape[current] = w
                g = str(state[x][e][2])

                if g == "L":
                    current = current - 1

                if g == "R":
                    current = current + 1

                x = int(state[x][e][3])
                print(x)
                print(e)
                print(current)
                print("tc=" + str(tape))
                if x == 6 and e == 1:
                    leaveLoop = "1000"

    print("Success!!")


def main():
    tape = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '1', '1', '1', '0', '1', '1', '0', 'B', 'B', 'B',
            'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
            'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
    comparison(tape)


if __name__ == '__main__':
    main()
