input_file = "input.txt"

with open(input_file) as file:
    data = file.read()

    elfes = data.split("\n\n")
    elfes = [elf.split("\n") for elf in elfes]
    elfes = [sum([int(item) for item in elf]) for elf in elfes]

    heaviest_elf = max(elfes)

    print(heaviest_elf)