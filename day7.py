import re
from collections import defaultdict

f = open("aoc\\day7_input.txt")
rules = f.read().split('\n')



def make_dict(rules):
    bag_rules = {}
    for rule in rules:
        parent, child = rule.split(" bags contain ")
        bag_rules[parent] = re.findall(r'([0-9]+) ([a-z ]+) bag', child.strip())
    return bag_rules

#print(make_dict(rules))
bag_rules = make_dict(rules)

def count_targetbag(bag_rules, target_bag):
    
    inverse_bag = defaultdict(list)

    for parent, child in bag_rules.items():
        for num, bag in child:
            if bag not in inverse_bag.keys():
                inverse_bag[bag] = [parent]
            inverse_bag[bag].append(parent)
    
    t_bags = set()
    temp_stack = [target_bag]

    while temp_stack:
        new_bag = temp_stack.pop()
        for parents in inverse_bag[new_bag]:
            if parents not in t_bags:
                t_bags.add(parents)
                temp_stack.append(parents)
    return len(t_bags) 


print(count_targetbag(bag_rules, "shiny gold"))

def count_sumbags()

