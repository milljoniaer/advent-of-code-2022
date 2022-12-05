import re

input_file = "input.txt"

with open(input_file) as file:
    data = file.read()

    data = data.split("\n\n")
    initial_state = data[0].split("\n")
    insturctions = data[1].split("\n")

    stacks = [[] for _ in filter(lambda c: c != "", initial_state[-1].split(" "))]
    for line in initial_state[0:-1]:
        for i in range(1,len(line), 4):
            if line[i] != " ":
                stack_index = (i-1)/4
                stacks[int(stack_index)].insert(0, line[i])
    
    for instr in insturctions:
        ret = re.match("move (\d*) from (\d*) to (\d*)", instr)
        [count, a, b] = ret.groups()

        for _ in range(int(count)):
            stacks[int(b)-1].append(stacks[int(a)-1].pop())

    tops = [stack[-1] for stack in stacks]

    print("".join(tops))