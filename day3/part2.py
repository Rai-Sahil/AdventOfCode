import re

def get_mul1(string):
    ans = 0
    pick_next = True
    i = 0

    while i < len(string):
        if string[i:i+7] == "don't()":
            pick_next = False
            i += 7
            continue

        elif string[i:i+4] == "do()":
            pick_next = True
            i += 4
            continue

        elif string[i:i+4] == "mul(":
            j = i + 4
            while j < len(string) and string[j] != ")":
                j += 1

            try:
                x, y = map(int, re.findall(r"\d+", string[i:j+1]))
                if pick_next and string[j-1] in ['1', '2', '3', '4',
                                                '5', '6', '7', '8',
                                                '9', '0']:
                        ans += (x * y)
            except:
                pass
            i += 1
        else:
            i += 1

    print(ans)

def get_mul2(file_path):
    # Regular expressions to match `mul(number, number)`, `do()`, and `don't()`
    mul_pattern = r"mul\((\d+),(\d+)\)"
    enable_pattern = r"do\(\)"
    disable_pattern = r"don't\(\)"

    # Read the entire file
    with open(file_path, 'r') as file:
        data = file.read()

    # Initialize variables
    is_enabled = True  # `mul` is enabled by default
    total_sum = 0

    # Split the input into tokens
    tokens = re.split(r"(?<=\))", data)  # Split after each closing parenthesis

    # Process each token
    for token in tokens:
        token = token.strip()  # Clean up whitespace

        # Check for enable or disable instructions
        if re.search(enable_pattern, token):
            is_enabled = True
        elif re.search(disable_pattern, token):
            is_enabled = False
        elif is_enabled:  # Process `mul` only if enabled
            mul_matches = re.findall(mul_pattern, token)
            for match in mul_matches:
                num1, num2 = map(int, match)
                total_sum += num1 * num2

    return total_sum


# Path to the input file
file_path = "input.txt"

# Calculate the result
result = get_mul2(file_path)

print(f"The total sum of all enabled multiplications is: {result}")

