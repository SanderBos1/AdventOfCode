from src.defaultCode import read_input
from collections import defaultdict


def common_5(test):
    lines = read_input("2024/opdracht5.txt", test)
    switch = False
    rules = []
    updates = []
    rules_dict = defaultdict(set)
    for i in range(len(lines)):
        if lines[i] == "":
            switch = True
            continue
        if switch:
            line = [int(x) for x in lines[i].split(",")]
            updates.append(line)
        else:
            rules.append(lines[i])
    for rule in rules:
        rule = rule.split("|")
        key = int(rule[1])
        rules_dict[key].add(int(rule[0]))
    return rules_dict, updates


def part_5a(test=False):
    total = 0
    rules_dict, updates = common_5(test)
    for update in updates:
        correct = True
        for i, item in enumerate(update):
            forbidden = rules_dict[item]
            if not all(future_item not in forbidden for future_item in update[i+1:]):
                correct = False
        if correct:
            total += update[(len(update) - 1) // 2]
    return total


def part_5b(test=False):
    total = 0
    rules_dict, updates = common_5(test)
    for update in updates:
        i = 0
        incorrect = False
        while i < len(update)-1:
            for j in range(i + 1, len(update)):
                forbidden = rules_dict[update[i]]
                if update[j] in forbidden:
                    incorrect = True
                    update[i], update[j] = update[j], update[i]
                    i = 0
            i += 1
        if incorrect:
            total += update[(len(update) - 1) // 2]
    return total
