def get_size():
    print("Enter puzzle size: ")
    n = int(input())
    return n


def print_grid(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def is_used_in_col(arr, col, num):
    for i in range(N):
        if arr[i][col] == num:
            return True
    return False


def is_safe_location(arr, row, col, num):
    return not is_used_in_row(arr, row, num) and not is_used_in_col(arr, col, num)


def find_empty_location(arr, l):
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def is_less_than(arr):
    for row in range(0, N, 2):
        for col in range(N - 1):
            if (arr[row][col] == '<') and (arr[row][col - 1] > arr[row][col + 1]):
                return False
    return True


def is_above(arr, col):
    for i in range(N - 1):
        if (arr[i][col] == '^') and (arr[i + 1][col] < arr[i - 1][col]):
            return False
    return True


def is_below(arr, col):
    for i in range(1, N - 1):
        if (arr[i][col] == 'v') and (arr[i + 1][col] > arr[i - 1][col]):
            return False
    return True


def is_used_in_row(arr, row, num):
    for i in range(N):
        if arr[row][i] == num:
            return True
    return False


def is_greater_than(arr):
    for row in range(0, N, 2):
        for col in range(N - 1):
            if (arr[row][col] == '>') and (arr[row][col - 1] < arr[row][col + 1]):
                return False
    return True


def solve(arr):
    l = [0, 0]
    if not find_empty_location(arr, l):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, n+1):
        if is_safe_location(arr, row, col, num):
            arr[row][col] = num
            if solve(arr):
                return True
            arr[row][col] = 0
    return False


def above_below_check(arr):
    for j in range(0, N, 2):
        if (is_below(arr, j) and is_above(arr, j)):
           return True
    return False


def get_puzzle(N):
    grid = []
    print("enter the entries row wise: ")
    for i in range(N):
        row = list(input().split())
        grid.append(row)
    return grid


def make_int(grid):
    for i in range(N):
        for j in range(N):
            if i % 2 == 0 and j % 2 == 0:
                grid[i][j] = int(grid[i][j])
    return grid


def futoshiki():
    grid = get_puzzle(N)
    grid = make_int(grid)
    print("Solution:")
    if solve(grid) and is_less_than(grid) and is_greater_than(grid) and above_below_check(grid):
        print_grid(grid)
    else:
        print("not possible")

    
n = get_size()
N = 2 * n - 1    
futoshiki()

