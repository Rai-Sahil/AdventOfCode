import re

# Way 1: Getting the answer using straight forward regex
def get_mul2(string):
    ans = 0
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, string)

    for match in matches:
        x, y = map(int, match)
        ans += (x * y)

    print(ans)

# Way 2: Getting the answer with iteration.
def get_mul1(string: str):
    ans = 0

    for i in range(len(string)):
        if string[i:i+4] == "mul(":
            j = i + 4
            while string[j] != ')':
                j += 1

            try:
                x, y = map(int, re.findall("(\d+)", string[i:j+1]))
                if string[j-1] not in ['1', '2', '3', '4', '5', '5', '6', '7', '8', '9', '0']:
                    continue
                ans += (x * y)
            except:
                pass

    print(ans)

def main():
    file_name = "input.txt"

    with open(file_name, 'r') as file:
        line = file.read()
        # Iterative way
        get_mul1(line)

        # Simple regex way
        get_mul2(line)

if __name__ == "__main__":
    main()
