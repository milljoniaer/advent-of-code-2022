input_file = "input.txt"

def start_of_cycle(finished_cycles, sprite):
    print(f'{sprite}     {finished_cycles}')
    if finished_cycles%40 in sprite:
            return "#"
    else:
        return "."


with open(input_file) as file:
    commands = file.read().split("\n")

    finished_cycles = 0
    X = 1

    sprite = range(0,3)

    out = []

    for cmd in commands:
        out.append(start_of_cycle(finished_cycles, sprite))

        if cmd == "noop":
            finished_cycles += 1
        elif cmd.split(" ")[0] == "addx":
            finished_cycles += 1
            out.append(start_of_cycle(finished_cycles, sprite))

            V = int(cmd.split(" ")[1])
            finished_cycles += 1
            X += V
            sprite = range(X-1,X+2)

    print(len(out))

    out = ["".join(out[i:i+40]) for i in range(0, len(out), 40)]
    out = "\n".join(out)

    print(out)
    print(finished_cycles)

