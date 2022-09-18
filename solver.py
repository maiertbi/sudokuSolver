import numpy as np

grid = [[5, 8, 6, 0, 3, 1, 0, 7, 0],
        [2, 0, 7, 8, 6, 0, 5, 1, 3],
        [0, 1, 0, 7, 0, 5, 2, 0, 6],
        [0, 2, 8, 0, 0, 4, 3, 6, 1],
        [6, 0, 4, 9, 1, 3, 7, 2, 0],
        [0, 3, 1, 6, 2, 0, 0, 9, 5],
        [4, 0, 5, 0, 8, 2, 0, 3, 7],
        [1, 7, 0, 4, 9, 6, 8, 0, 2],
        [0, 6, 2, 3, 5, 0, 1, 0, 9]]


def printGrid(gr):
    print(np.array(gr))


def validateNumber(y, x, n):
    global grid

    for i in range(len(grid)):
        if grid[i][x] == n or grid[y][i] == n:  # proves y and x axis simultaneously
            return False

    box_start_y = y // 3 * 3
    box_start_x = x // 3 * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[box_start_y + i][box_start_x + j] == n:  # checks each smaller box
                return False
    return True


def solve(gr):
    for y in range(len(gr)):  # y-axis
        for x in range(len(gr)):  # x-axis
            if gr[y][x] != 0:
                continue
            for n in range(1, 10):
                if validateNumber(y, x, n):
                    gr[y][x] = n
                    solve(gr)  # recursion happens here
                    gr[y][x] = 0
            return
    printGrid(gr)


def main():
    solve(grid)


if __name__ == '__main__':
    main()
