from itertools import combinations

f = open("aoc\\day9_input.txt")

example = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]

seq = f.read().split("\n")
seq = [int(x) for x in seq]


def find_wrong(seq, pre):
    
    for n, s in enumerate(seq):

        if n+pre == len(seq):
            return 0
        sub_seq = seq[n:n+pre]
        flag = False

        for c in combinations(sub_seq, 2):
            if sum(c) == seq[n+pre]:
                flag = True
        if not flag:
            return(seq[n+pre], n+pre)

print(find_wrong(seq, 25))
print(find_wrong(example, 5))


def enc_weakness(seq, wrong_ans, wrong_pos):
    left = 0
    right = 0
    while(sum(seq[left: left + right + 2]) != wrong_ans):
        if sum(seq[left: left + right + 2]) <= wrong_ans:
            right +=1 
        else:
            left +=1 
            right = 0 

    return min(seq[left:left + right +2])+ max(seq[left:left + right + 2])

print(enc_weakness(seq, 466456641 , 611))
