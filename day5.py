from math import floor, ceil

f = open("aoc\\day5_input.txt")
txt = f.read().split("\n")


def get_seatid(txt):
    
    ids =[]

    for seats in txt:

        r_left = 0 
        r_right = 127

        for letter in seats[:-4]:
            mid = (r_left + r_right) // 2
            if letter == "F" :
                r_right = mid 
            else:
                r_left = mid +1
        
        if(seats[-4] == "F" ):
            row = r_left
        else:
            row = r_right

        c_left = 0 
        c_right = 7

        for letter in seats[-3:-1]:
            mid = (c_left + c_right) // 2
            if letter == "L":
                c_right = mid
            else:
                c_left = mid + 1
        if (seats[-1] == "L"):
            col = c_left 
        else:
            col = c_right
        
        sid = row*8 + col
        ids.append(sid)
    
    return max(ids)

print(get_seatid(txt))

def get_seatid2(txt):
    
    ids =[]

    for seats in txt:

        r_left = 0 
        r_right = 127

        for letter in seats[:-4]:
            mid = (r_left + r_right) // 2
            if letter == "F" :
                r_right = mid 
            else:
                r_left = mid +1
        
        if(seats[-4] == "F" ):
            row = r_left
        else:
            row = r_right

        c_left = 0 
        c_right = 7

        for letter in seats[-3:-1]:
            mid = (c_left + c_right) // 2
            if letter == "L":
                c_right = mid
            else:
                c_left = mid + 1
        if (seats[-1] == "L"):
            col = c_left 
        else:
            col = c_right
        
        sid = row*8 + col
        ids.append(sid)
    
    sorted_id = sorted(ids)
    for i in range(len(sorted_id)-1):
        if sorted_id[i] + 2 == sorted_id[i+1]:
            return sorted_id[i] +1
    
    return -1

print(get_seatid2(txt))









            


