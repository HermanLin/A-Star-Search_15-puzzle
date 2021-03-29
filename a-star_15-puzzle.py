from shutil import copyfile

# read and process an input file for the initial and goal states
def processFile (filename):
    f = open(filename, 'r')
    # read 4 lines and remove trailing newlines for initial and goal
    initial = [next(f).rstrip() for line in range(4)]
    next(f) # skip blank line
    goal = [next(f).rstrip() for line in range(4)]
    f.close()

    # turn into 2d lists
    initial = [row.split(' ') for row in initial]
    goal = [row.split(' ') for row in goal]

    return initial, goal

# returns the sum of chessboard distances from goal 
# positions as the heuristic function 
def heuristic(initial, goal):
    # chessboard distance heuristic = max(h, v) moves
    sum_cd = 0

    # loop through initial state, compare to goal state
    for i in range(0, 4):
        for j in range(0, 4): # loop through all initial tiles
            init_tile = initial[i][j]
            for v_moves in range(0, 4):
                for h_moves in range(0, 4): # loop through all goal tiles
                    if init_tile == goal[v_moves][h_moves]:
                        # choose max between vertical and horizontal moves
                        sum_cd += max(abs(v_moves - i), abs(h_moves - j))
    return sum_cd

def main():
    filename = input()
    i, g = processFile(filename)
    print(i)
    print(g)

    print(heuristic(i, g))


main()