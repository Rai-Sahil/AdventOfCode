
def find_path(lines):
    stack = []
    visited = set()

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '^':
                stack.append((row, col, -1, 0))
                break

    dis1, dis2 =0, 0
    while stack:
        row, col, dr, dc = stack.pop()

        while (row+dr) >= 0 and (col+dc) >= 0 and (row+dr) < len(lines) and (col+dc) < len(lines[0]):
            if lines[row+dr][col+dc] == '#':
                if dr == -1 and dc == 0:
                    dr, dc = 0, 1
                elif dr == 0 and dc == 1:
                    dr, dc = 1, 0
                elif dr == 1 and dc == 0:
                    dr, dc = 0, -1
                elif dr == 0 and dc == -1:
                    dr, dc = -1, 0

                stack.append((row, col, dr, dc))
                break
            else:
                row, col = row + dr, col + dc
                
                dis1 = dis1 + dr
                dis2 = dis2 + dc
                # print(dis1, dis2)
                if (dis1, dis2) in visited:
                    print(row, col)
                
                visited.add((dis1, dis2))
    
def main():
    file_path = "input.txt"

    with open(file_path, 'r') as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
        find_path(grid)

if __name__ == "__main__":
    main()


