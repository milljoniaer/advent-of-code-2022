input_file = "input.txt"

def get_shapes_score(shape):
    if shape == "X":
        return 1
    elif shape == "Y":
        return 2
    else:
        return 3

with open(input_file) as file:
    data = file.read().replace("A", "X").replace("B", "Y").replace("C", "Z")
    rounds = data.split("\n")

    score_sum = 0
    for round in rounds:
        shapes = round.split(" ")
        him = shapes[0]
        me = shapes[1]
        
        i_win = (him == "Z" and me == "X") or (him == "X" and me == "Y") or (him == "Y" and me == "Z")
        if him == me:
            score_sum += 3 + get_shapes_score(me)
            continue
        elif i_win:
            score_sum += 6 + get_shapes_score(me)
        else:
            score_sum += get_shapes_score(me)

    print(score_sum)