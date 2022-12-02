input_file = "input.txt"

def get_shapes_score(shape):
    if shape == "X":
        return 1
    elif shape == "Y":
        return 2
    else:
        return 3

def equals(one, two):
    return (one == "A" and two == "X") or (one == "B" and two == "Y") or (one == "C" and two == "Z")

def loose(him):
    if him == "A": return "Z"
    elif him == "B": return "X"
    else: return "Y"

def drawn(him):
    if him == "A": return "X"
    elif him == "B": return "Y"
    else: return "Z"

def win(him): 
    if him == "A": return "Y"
    elif him == "B": return "Z"
    else: return "X"

def what_to_do(him, winning): 
    if winning == "X": return loose(him)
    elif winning == "Y": return drawn(him)
    else: return win(him)

with open(input_file) as file:
    data = file.read()
    rounds = data.split("\n")

    score_sum = 0
    for round in rounds:
        shapes = round.split(" ")
        him = shapes[0]
        me = what_to_do(him, shapes[1])
        
        i_win = (him == "C" and me == "X") or (him == "A" and me == "Y") or (him == "B" and me == "Z")
        if equals(him, me):
            score_sum += 3 + get_shapes_score(me)
            continue
        elif i_win:
            score_sum += 6 + get_shapes_score(me)
        else:
            score_sum += get_shapes_score(me)

    print(score_sum)