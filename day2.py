f = open("aoc\\day2_input.txt")
x = f.read().splitlines()


temp = [t.split(":") for t in x]

def pass_checker(lst):
    cont = lst[0]
    passs = lst[1]

    min_1 = list(map(int, cont.split()[0].split("-")))[0]
    max_1 = list(map(int, cont.split()[0].split("-")))[1]
    letter = cont.split()[1]

    num = passs.count(letter)

    if((num >= min_1) and (num <= max_1)):
        return True
    else:
        return False


count = 0
for t in temp:
    if(pass_checker(t)):
        count += 1

print(count)

def pass_checker2(lst):
    cont = lst[0]
    passs = lst[1]

    pos_1 = list(map(int, cont.split()[0].split("-")))[0]
    pos_2 = list(map(int, cont.split()[0].split("-")))[1]
    letter = cont.split()[1]

    if(((passs[pos_1] == letter) and not(passs[pos_2]== letter)) or (not(passs[pos_1] == letter) and (passs[pos_2]== letter))):
        return True
    else:
        return False

count = 0
for t in temp:
    if(pass_checker2(t)):
        count += 1

print(count)