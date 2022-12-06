import sys


input_file = "input.txt"


with open(input_file) as file:
    stream = file.read()
    for i in range(4,len(stream)):
        four_cs = stream[i-4:i]
        if len(set(four_cs)) == 4:
            print(i)
            sys.exit(0)



