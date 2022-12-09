input_file = "input.txt"


with open(input_file) as file:
    instructions = file.read().split("\n")

    rope = [[0,0] for _ in range(10)]

    pos = ["00"]
    for instr in instructions:
        spl = instr.split(" ")
        direction = spl[0]
        steps = int(spl[1])

        for _ in range(steps):
            # update head (rope[0])
            if direction == "R":
                rope[0][0] = rope[0][0] + 1 # increase x
            elif direction == "L":
                rope[0][0] = rope[0][0] - 1 # decrease x
            elif direction == "U":
                rope[0][1] = rope[0][1] + 1 # increase y
            elif direction == "D":
                rope[0][1] = rope[0][1] - 1 # decrease y

            # update rest of the rope
            for i in range(1,len(rope)):
                H = rope[i-1]
                T = rope[i]
                if abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1:
                    if abs(H[0]-T[0]) > 1:
                        T[0] = (H[0]+T[0])//2
                        T[1] = H[1]
                    elif abs(H[1]-T[1]) > 1:
                        T[1] = (H[1]+T[1])//2
                        T[0] = H[0]
                    
            # save hashed coordinate of last rope node
            pos.append(f'{rope[-1][0]}{rope[-1][1]}')

    distinct_pos = list(set(pos))
    print(len(distinct_pos))

            




