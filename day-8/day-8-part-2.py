input_file = "input.txt"

def visible_trees_top(field, y, x):
    count = 0
    for i in range(y-1, -1, -1):
        count = count + 1
        if field[i][x] >= field[y][x]:
            break

    return count

def visible_trees_right(field, y, x):
    count = 0
    for i in range(min(len(field[0]), x+1), len(field[0])):
        count = count + 1
        if field[y][i] >= field[y][x]:
            break
    return count

def visible_trees_bottom(field, y, x):
    count = 0
    for i in range(min(len(field), y+1), len(field)):
        count = count + 1
        if field[i][x] >= field[y][x]:
            break
    return count

def visible_trees_left(field, y, x):
    count = 0
    for i in range(x-1, -1, -1):
        count = count + 1
        if field[y][i] >= field[y][x]:
            break
    return count

def visible(field, y, x):
    return visible_trees_top(field, y, x) * visible_trees_right(field, y, x) * visible_trees_bottom(field, y, x) * visible_trees_left(field, y, x)

with open(input_file) as file:
    field = file.read().split("\n")
    
    sights = []
    for y in range(len(field)):
        for x in range(len(field[0])):
            sights.append(visible(field, y, x))

    print(max(sights))



