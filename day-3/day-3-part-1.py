input_file = "input.txt"

def get_weight(c):
    c = ord(c)
    if c > 64 and c < 91:
        return c - 64 + 26
    else:
        return c - 96

with open(input_file) as file:
    data = file.read()

    bags = data.split("\n")
    bags = [[b[:len(b)//2], b[len(b)//2:]] for b in bags]

    doubles = []
    for b in bags:
        com_1 = b[0]
        com_2 =b[1]

        to_add = []

        for c in com_1:
            if com_2.find(c) != -1:
                to_add.append(get_weight(c))

        to_add = list(set(to_add))
        doubles = doubles + to_add

    print(sum(doubles))