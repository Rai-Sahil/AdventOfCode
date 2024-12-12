def main():
    file_name = "input.txt"
    safe_count = 0

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            numbers = list(map(int, line.split()))

            inc_or_dec = (numbers==sorted(numbers) or numbers==sorted(numbers,reverse=True))
            ok = True

            for i in range(len(numbers) - 1):
                dis = abs(numbers[i] - numbers[i+1])
                if dis > 3 or dis < 1:
                    ok = False

            if ok and inc_or_dec:
                safe_count += 1
                    
    print(safe_count)

if __name__ == "__main__":
    main()
