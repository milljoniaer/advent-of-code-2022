input_file = "input-test.txt"


with open(input_file) as file:
    instructions = file.read().split("\n")

    H = [0,0]
    T = [0,0]

    pos = ["00"]
    for instr in instructions:
        spl = instr.split(" ")
        direction = spl[0]
        steps = int(spl[1])

        for _ in range(steps):
            if direction == "R":
                H[0] = H[0] + 1 # increase x
            elif direction == "L":
                H[0] = H[0] - 1 # decrease x
            elif direction == "U":
                H[1] = H[1] + 1 # increase y
            elif direction == "D":
                H[1] = H[1] - 1 # decrease y

            if abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1:
                if abs(H[0]-T[0]) > 1:
                    T[0] = (H[0]+T[0])//2
                    T[1] = H[1]
                elif abs(H[1]-T[1]) > 1:
                    T[1] = (H[1]+T[1])//2
                    T[0] = H[0]
                
                pos.append(f'{T[0]}{T[1]}')

            print(f'H {H}; T {T}')


    distinct_pos = list(set(pos))
    print(len(distinct_pos))

            




