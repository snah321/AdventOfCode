import re

f = open("aoc\\day4_input.txt")
txt = f.read().split("\n\n")


temp = txt[1].replace("\n", " ").split()
ans = dict(t.split(":") for t in temp)
print(ans['hgt'][:-2])


req = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
                     (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.fullmatch(r"#[\da-f]{6}", x),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: re.fullmatch(r"\d{9}", x),
}

temp2 = dict(item.split(":") for item in txt[0].replace("\n", " ").split())
print(temp2)
print(all(t in temp2.keys() for t in req))




def valid_pass(txt, req):

    present = 0
    valid = 0

    for t in txt:
        temp = dict(item.split(":") for item in t.replace("\n", " ").split())
    
        if not(len(temp.keys()) >= len(req.keys())):
            continue

        if all(k in temp.keys() for k in req.keys()):
            present += 1
        
            if all(value(temp[key]) for key, value in req.items()):
                valid +=1
                       
            
    
    return present, valid



print(valid_pass(txt, req))


        