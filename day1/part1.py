def main():
    file_path = "input.txt"

    first_arr, second_arr = [], []

    with open(file_path, 'r') as file:
        for line in file:
            first, second = map(int, line.split())
            first_arr.append(first)
            second_arr.append(second)

    first_arr.sort()
    second_arr.sort()

    final_distance = 0

    for i in range(len(first_arr)):
        final_distance += abs(first_arr[i] - second_arr[i])

    print(final_distance)

if __name__ == "__main__":
    main()
