
def find_xmas(grid):
    dir = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]    
    stack = []
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                stack.append((row, col, 1, -2, -2))
    
    while len(stack) != 0:
        r, c, left, rw, cl = stack.pop(0)
        
        if rw == -2 and cl == -2:
            for dx, dy in dir:
                dr = r + dx
                dc = c + dy
                
                if left < 3 and dr < len(grid) and dc < len(grid[0]) and dr >= 0 and dc >= 0:
                    if grid[dr][dc] == 'M':
                        stack.append((dr, dc, left + 1, dx, dy))
            
        else:
            dr, dc = r+rw, c+cl
            if left > 3 or dr >= len(grid) or dc >= len(grid[0]) or dr < 0 or dc < 0:
                continue
            if left < 3 and grid[dr][dc] == 'A':
                stack.append((dr, dc, left + 1, rw, cl))
            elif left == 3 and grid[dr][dc] == 'S':
                count += 1            

    print(count)

def main():
    file_name = "input.txt"

    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        grid = [list(line.strip()) for line in lines]

        find_xmas(grid)
        

if __name__ == "__main__":
    main()
