def check_line(arr):
    inc_or_dec = ((arr == sorted(arr)) or arr == sorted(arr, reverse=True))
    ok = True

    for i in range(len(arr) - 1):
        distance = abs(arr[i] - arr[i+1])
        if distance < 1 or distance > 3:
            ok = False

    return inc_or_dec and ok

def main():
    file_name = "input.txt"
    answer2 = 0
    answer1 = 0

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            numbers = list(map(int, line.split()))
            good = False
            
            if check_line(numbers):
                answer1 += 1

            for i in range(len(numbers)):
                arr = numbers[:i] + numbers[i+1:]
                if check_line(arr):
                    good = True

            if good:
                answer2 += 1

    print(answer1)
    print(answer2)

main()
