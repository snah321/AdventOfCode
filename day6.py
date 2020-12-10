

f = open("aoc\\day6_input.txt")
txt = f.read().split("\n\n")


txt = [t.split("\n") for t in txt]

def sumcounts(txt):
    
    counts = []

    for ans in txt:
        sets = set()
        for word in ans:
            for char in word:
                if not(char in sets ):
                    sets.add(char)
        counts.append(len(sets))
    return sum(counts)
    

print(sumcounts(txt))

def sumall(txt):
    
    counts = [] 

    for ans in txt:
        lst = [] 
        for word in ans:
            setl = set()
            for char in word:
                setl.add(char)
            lst.append(setl)
        
        count = len(set.intersection(*lst))
        counts.append(count)
    
    return sum(counts)

print(sumall(txt))