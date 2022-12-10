input_file = "input.txt"


with open(input_file) as file:
    commands = file.read().split("\n")

    finished_cycles = 0
    X = 1

    Xs = []
    for cmd in commands:
        Xs.append(X)

        if cmd == "noop":
            finished_cycles += 1
        elif cmd.split(" ")[0] == "addx":
            Xs.append(X)
            V = int(cmd.split(" ")[1])
            finished_cycles += 2
            X += V

    values = [Xs[i] * (i+1) for i in range(19, len(Xs), 40)]

    print(f'{X} . {finished_cycles}')
    print(sum(values))
