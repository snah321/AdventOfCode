from copy import deepcopy

f = open("aoc\\day11_input.txt")

seat_grid = f.read().split('\n')
seat_grid = [list(x) for x in seat_grid]

move = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

rows = len(seat_grid)
cols = len(seat_grid[0])

def adj_seat(grid, row, col):
    occupied_seats = 0
    for x,y in move:
        new_row = row + x
        new_col = col + y

        if not (0 <= new_row < rows and 0 <= new_col < cols):
            continue
        if grid[new_row][new_col] == "#":
            occupied_seats += 1

    return occupied_seats

def transform_grid(grid, num_occupied = 4):

    new_grid = deepcopy(grid)

    for row in range(rows):
        for col in range(cols):
            occupied_seats = adj_seat(grid, row, col)

            if grid[row][col] == "L" and occupied_seats == 0:
                new_grid[row][col] = "#"
            elif grid[row][col] == "#" and occupied_seats >= num_occupied:
                new_grid[row][col] = "L"
    
    return new_grid

def sum_occupied_seats(grid):
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                count += 1
    return count


def solve_p1(grid):

    prev_occupied = -1 
    curr_occupied = sum_occupied_seats(grid)
    
    while prev_occupied != curr_occupied:
        prev_occupied = curr_occupied
        new_seat = transform_grid(grid)
        curr_occupied = sum_occupied_seats(new_seat)
        grid = new_seat
    return prev_occupied, curr_occupied

#print(solve_p1(seat_grid))

def new_adj(grid, row, col):
    occupied_seats = 0
    for x,y in move:
        new_row = row + x
        new_col = col + y

        while (0 <= new_row < rows and 0 <= new_col < cols) and  (grid[new_row][new_col] == ".") :
            new_row = new_row + x
            new_col = new_col + y
        if (0 <= new_row < rows and 0 <= new_col < cols) and (grid[new_row][new_col] == "#" ):
            occupied_seats += 1 
    return occupied_seats

def new_transform_grid(grid, num_occupied = 5):
    new_grid = deepcopy(grid)

    for row in range(rows):
        for col in range(cols):
            occupied_seats = new_adj(grid, row, col)

            if grid[row][col] == "L" and occupied_seats == 0:
                new_grid[row][col] = "#"
            elif grid[row][col] == "#" and occupied_seats >= num_occupied:
                new_grid[row][col] = "L"
    
    return new_grid




def solve_p2(grid):

    prev_occupied = -1 
    curr_occupied = sum_occupied_seats(grid)

    while prev_occupied != curr_occupied:
        prev_occupied = curr_occupied
        new_seat = new_transform_grid(grid)
        curr_occupied = sum_occupied_seats(new_seat)
        grid = new_seat
    return prev_occupied, curr_occupied

print(solve_p2(seat_grid))

