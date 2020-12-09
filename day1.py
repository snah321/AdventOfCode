from itertools import combinations
import math




f = open("E:\\Downloads\\aoc\\day1_input.txt")

x = map(int,f.read().split())


def solver(list1, n):
    for c in combinations(list1, n):
        if(sum(c) == 2020):
            return (math.prod(c))

#print(solver(x,2))

print(solver(x,3))