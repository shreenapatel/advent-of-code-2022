from copy import copy
from math import floor


def monkey_around(value, operation_string):
    """Perform monkey's operation from string"""

    old = copy(value)  # noqa

    return eval(operation_string)


def collect_monkey_attributes(monkey_data):
    """Extract monkey attributes from raw text and
    return as dict"""

    monkey = {}

    lines = monkey_data.split("\n")
    monkey["items"] = [
        int(x)
        for x in lines[1].replace("Starting items:", "").replace(" ", "").split(",")
    ]
    monkey["operation"] = lines[2].replace("  Operation: new = ", "")
    monkey["test_factor"] = int(lines[3].split("divisible by")[-1])
    monkey["test_pass"] = int(lines[4].split("monkey ")[-1])
    monkey["test_fail"] = int(lines[5].split("monkey ")[-1])

    return monkey


def part1(data):

    monkeys = {}
    for i, monkey_data in enumerate(data.rstrip("\n").split("\n\n")):
        monkeys[i] = collect_monkey_attributes(monkey_data)

    num_items_by_monkey = [0 for k in monkeys.keys()]

    for _ in range(20):

        for i, monkey in monkeys.items():

            # Update worry levels for items the monkey currently has
            worry_levels = [
                floor(monkey_around(x, monkey["operation"]) / 3)
                for x in monkey["items"]
            ]

            # Update item assignments based on divisibility by test_factor
            items_pass = [
                worry_level
                for worry_level in worry_levels
                if worry_level % monkey["test_factor"] == 0
            ]
            items_fail = [
                worry_level
                for worry_level in worry_levels
                if worry_level % monkey["test_factor"] != 0
            ]
            monkeys[monkey["test_pass"]]["items"] += items_pass
            monkeys[monkey["test_fail"]]["items"] += items_fail
            # Current monkey now has no items
            monkeys[i]["items"] = []

            num_items_by_monkey[i] += len(worry_levels)

    num_items_by_monkey.sort(reverse=True)

    return num_items_by_monkey[0] * num_items_by_monkey[1]


def part2(data):
    monkeys = {}
    for i, monkey_data in enumerate(data.rstrip("\n").split("\n\n")):
        monkeys[i] = collect_monkey_attributes(monkey_data)

    # Worry levels get pretty large as the number of rounds increase,
    # so need to take modulus to shrink numbers. The divisor is
    # found by multiplying all the test factors
    mod_div = 1
    for m, monkey in monkeys.items():
        mod_div = mod_div * monkey["test_factor"]

    num_items_by_monkey = [0 for _ in monkeys.keys()]

    for _ in range(10000):

        if _ % 1000 == 0:
            print(f"Round {_}")

        for i, monkey in monkeys.items():

            # Update worry levels for items the monkey currently has
            worry_levels = [
                monkey_around(w, monkey["operation"]) % mod_div for w in monkey["items"]
            ]

            # Update item assignments based on divisibility by test_factor
            items_pass = [
                worry_level
                for worry_level in worry_levels
                if worry_level % monkey["test_factor"] == 0
            ]
            items_fail = [
                worry_level
                for worry_level in worry_levels
                if worry_level % monkey["test_factor"] != 0
            ]
            monkeys[monkey["test_pass"]]["items"] += items_pass
            monkeys[monkey["test_fail"]]["items"] += items_fail
            # Current monkey now has no items
            monkeys[i]["items"] = []

            num_items_by_monkey[i] += len(worry_levels)

    num_items_by_monkey.sort(reverse=True)

    return num_items_by_monkey[0] * num_items_by_monkey[1]
