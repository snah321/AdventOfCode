from collections import defaultdict

f = open("aoc\\day10_input.txt")

example = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3
]

ada = f.read().split("\n")
ada = [int(x) for x in ada]
#print(ada)

def diff_multi(ada):
    diff1 = 0 
    diff3 = 0

    sort_ada = sorted(ada)
    max_ada = max(sort_ada) + 3
    sort_ada.insert(0, 0)
    sort_ada.append(max_ada)

    for i in range(len(sort_ada) - 1 ):
        if (sort_ada[i+1] - sort_ada[i]) == 1 :
            diff1 += 1
        else:
            diff3 += 1
    return (diff1 * (diff3))

print(diff_multi(ada) )

sort_seq = sorted(ada)
max_ada = max(sort_seq) + 3
sort_seq.insert(0, 0)

print(sort_seq)

paths = defaultdict(int )
paths[0] = 1

# for adapter in sort_seq:
#     for diff in range(1, 4):
#         next_adapter = adapter + diff
#         if next_adapter in sort_seq:
#             paths[next_adapter] += paths[adapter]


def num_path(seq):

    for prev_adapter in seq:

        for d in range(1,4):
            next1 = prev_adapter + d
            if next1 in seq:
                paths[next1] += paths[prev_adapter]

    return paths[max(seq)]

print(num_path(sort_seq))

    
