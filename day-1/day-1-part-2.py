input_file = "input.txt"

with open(input_file) as file:
    data = file.read()

    elfes = data.split("\n\n")
    elfes = [elf.split("\n") for elf in elfes]
    elfes = [sum([int(item) for item in elf]) for elf in elfes]
    elfes.sort(reverse=True)

    top_three_elfes = elfes[0:3]
    top_three_sum = sum(top_three_elfes)
    print(top_three_elfes)
    print(top_three_sum)