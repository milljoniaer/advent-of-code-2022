input_file = "input.txt"
lines_per_group = 3

def get_weight(c):
    c = ord(c)
    if c > 64 and c < 91:
        return c - 64 + 26
    else:
        return c - 96

with open(input_file) as file:
    data = file.read()

    bags = data.split("\n")
    groups = [bags[i:i+lines_per_group] for i in range(0, len(bags), lines_per_group)]

    badges = []
    for group in groups:
        for c in group[0]:
            if group[1].find(c) != -1 and group[2].find(c) != -1:
                badges.append(get_weight(c))
                break

    print(sum(badges))