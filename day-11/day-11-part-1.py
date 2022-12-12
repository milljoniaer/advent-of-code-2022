
from functools import reduce


input_file = "input.txt"

with open(input_file) as file:
    monkeys = file.read().split("\n\n")
    monkeys = [monkey.split("\n") for monkey in monkeys]

    monkeyList = []

    print("Parsing Input...")

    for monkey in monkeys:
        items = (monkey[1].split(" "))
        items = [int(item.replace(",", "")) for item in items[4:]]
        operation = monkey[2].replace("  Operation: new = ", "")
        testNumber = int(monkey[3].split(" ")[-1])
        trueMonkey = int(monkey[4].split(" ")[-1])
        falseMonkey = int(monkey[5].split(" ")[-1])

        parsed_monkey = {
            "items": items,
            "operation": operation,
            "testNumber": testNumber,
            "trueMonkey": trueMonkey,
            "falseMonkey": falseMonkey,
            "inspections": 0
        }

        print(parsed_monkey)

        monkeyList.append(parsed_monkey)

    print("\n\nCalculating...")

    for _ in range(10000):
        print(_)
        for monkey in monkeyList:
            print("Monkey")
            for _ in range(len(monkey["items"])):
                monkey["inspections"] += 1
                item = monkey["items"].pop(0)
                operation = monkey["operation"]
                testNumber = monkey["testNumber"]

                # I know it is dangerous :)
                new_worry = int(eval(operation.replace("old", str(item))))
                new_worry = new_worry // 3

                if new_worry % testNumber == 0:
                    monkeyList[monkey["trueMonkey"]]["items"].append(new_worry)
                    print(f'item {new_worry} to {monkey["trueMonkey"]}')
                else:
                    monkeyList[monkey["falseMonkey"]]["items"].append(new_worry)
                    print(f'item {new_worry} to {monkey["falseMonkey"]}')

    monkey_activeness = sorted([monkey["inspections"] for monkey in monkeyList], reverse=True)
    monkey_activeness = monkey_activeness[0:2]
    business_level = reduce((lambda x,y: x*y), monkey_activeness)

    print(f'monkey bsuiness level: {business_level}')

