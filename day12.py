import re

f = open("aoc\\day12_input.txt") 

move = f.read().split("\n")
move = [re.findall(r'([A-Z]+)([0-9]+)', m) for m in move]
print(move)

class ferry:
    """
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

    """

    def __init__(self, loc):
        self.loc = loc
    def move
        
