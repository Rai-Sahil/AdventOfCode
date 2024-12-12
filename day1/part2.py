def main():
    file_path = "input.txt"

    first_arr, second_dict = [], {}

    with open(file_path, 'r') as file:
        for line in file:
            first, second = map(int, line.split())
            first_arr.append(first)
            
            if second in second_dict:
                second_dict[second] += 1
            else:
                second_dict[second] = 1
    
    similarity = 0

    for num in first_arr:
        similarity += second_dict[num] * num if num in second_dict else 0
    
    print(similarity)

if __name__ == "__main__":
    main()
