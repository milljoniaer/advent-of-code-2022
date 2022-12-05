input_file = "input.txt"


with open(input_file) as file:
    data = file.read()

    teams = data.split("\n")
    teams = [team.split(",") for team in teams]
    
    count = 0
    for team in teams:
        m_1 = team[0].split("-")
        m_2 = team[1].split("-")
        first = range(int(m_1[0]), int(m_1[1])+1)
        second = range(int(m_2[0]), int(m_2[1])+1)

        if any(e in first for e in second) or any(e in second for e in first):
            count = count + 1

    print(count)



