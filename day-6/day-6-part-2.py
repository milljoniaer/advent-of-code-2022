import sys


input_file = "input.txt"


with open(input_file) as file:
    stream = file.read()
    for i in range(14,len(stream)):
        four_cs = stream[i-14:i]
        if len(set(four_cs)) == 14:
            print(i)
            sys.exit(0)



