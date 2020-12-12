
f = open("aoc\\day8_input.txt")
code = f.read().split("\n")
print(code[-1].split(" "))


example = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]


def get_acc(code):

    acum = 0
    length = len(code) -1 
    visited = [0]*(length)
    curr = 0

    while visited[curr%length] != 1:
        
        visited[curr%length] = 1
        opr,num = code[curr%length].split(" ")
        
        if opr == "nop":
            curr += 1
        elif opr == "acc":
            acum += int(num)
            curr += 1
        elif opr == "jmp":
            curr += int(num)
    #final acum value and curr position that repeats twice
    return acum,curr

print(get_acc(example))



def fix_code(code):

    for n, c in enumerate(code):
        
        opr, num = c.split(" ")
        test = (0,0)

        if opr == "nop" or opr == "jmp":
            try_code = code[:]
            if opr == "nop":
                try_code[n] = "jmp" + " " + num
                #print(try_code[n], c)
            if opr == "jmp":
                try_code[n] = "nop" + " " + num
                #print(try_code[n], c)
            test = get_acc(try_code)
            if test[1] == (len(try_code) -1 ):
                return test
                break
        
print(fix_code(code))


