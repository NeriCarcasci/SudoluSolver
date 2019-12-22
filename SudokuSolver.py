board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

show_steps = 0
step_key = None

def solve(bo):
    
    

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    if show_steps == 1:
        print(bo)
    elif show_steps == 3:
        if (step_key -1) == row:
            print(bo[step_key-1])

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def steps_decider():
    global show_steps
    global step_key
    ans = input("Do you want to see the steps to solve this sudoku board?(Y or N)")
    ans = ans.lower()
    if ans == "y":
        show_steps = 1
    elif ans == "n":
        show_steps = 2
    elif "w" in ans:
        try:
            ans = ans.split("-")
            step_key = int(ans[1])
            print(ans)
            if step_key == 0:
                print(error)
            show_steps = 3

        except:
            print("answer did not contain required sintax")
            steps_decider()


    else:
        print("Answer Invalid try again")
        steps_decider()

steps_decider()
print_board(board)
print("________________________________\n")
solve(board)
print("________________________________\n")
print_board(board)

