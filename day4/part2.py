
def find_x_shape(grid):
    count = 0

    def check_mas(row, col):
        if (row+1) < len(grid) and (row-1) >= 0 and (col-1) >= 0 and (col+1) < len(grid) and grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S':
            if grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S':
                return True
            if grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M':
                return True
        
        if (row+1) < len(grid) and (row-1) >= 0 and (col-1) >= 0 and (col+1) < len(grid) and grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M':
            if grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S':
                return True
            if grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M':
                return True

        return False


    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'A':
                if check_mas(row, col):
                    count += 1

    print(count)

def main():
    file_name = "input.txt"

    with open(file_name, 'r') as file:
        lines = file.readlines()

        find_x_shape(lines)

if __name__ == "__main__":
    main()
