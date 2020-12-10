import math

f = open("aoc\\day3_input.txt")
grid = f.read().splitlines()



def down_slope(grid, x, y):
    
    trees = 0
    width = len(grid[0])
    height = len(grid)

    curr_x, curr_y = 0,0

    while curr_y < height:
        if(grid[curr_y][curr_x % width] == "#"):
            trees += 1
        curr_x += x
        curr_y += y 
    return trees


print(down_slope(grid, 3, 1))

args = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def prod_trees(grid, args):

    ans = []
    for xy in args:
        ans.append(down_slope(grid, *xy))
    return math.prod(ans)

print(prod_trees(grid, args))



