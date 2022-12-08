input_file = "input.txt"

def visible_top(field, y, x):
    for i in range(y-1, -1, -1):
        if field[i][x] >= field[y][x]:
            return False

    print(f'{field[y][x]} visible from TOP')
    return True

def visible_right(field, y, x):
    for i in range(min(len(field[0]), x+1), len(field[0])):
        if field[y][i] >= field[y][x]:
            return False
    print(f'{field[y][x]} visible from RIGHT')
    return True

def visible_bottom(field, y, x):
    for i in range(min(len(field), y+1), len(field)):
        if field[i][x] >= field[y][x]:
            return False
    print(f'{field[y][x]} visible from BOTTOM')
    return True

def visible_left(field, y, x):
    for i in range(x-1, -1, -1):
        if field[y][i] >= field[y][x]:
            return False
    print(f'{field[y][x]} visible from LEFT')
    return True

def visible(field, y, x):
    return visible_top(field, y, x) or visible_right(field, y, x) or visible_bottom(field, y, x) or visible_left(field, y, x)

with open(input_file) as file:
    field = file.read().split("\n")
    
    count = 0
    for y in range(len(field)):
        for x in range(len(field[0])):
            if visible(field, y, x):
                count = count + 1 

    print(count)



