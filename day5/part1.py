import collections

def print_pages(pages, outputs):
    adj = collections.defaultdict(list)
    orders = []
    sum = 0

    for line in pages:
        line.strip()

        a, b = map(int, line.split('|'))
        adj[b].append(a) 
   
    for output in outputs:
        found = True
        for i in range(len(output) - 1, 0, -1):
            if output[i] in adj:
                if output[i-1] not in adj[output[i]]:
                    found = False
            else:
                found = False

        if found:
            orders.append(output)

    for order in orders:
        middle_index = len(order) // 2
        sum += order[middle_index]

    print(sum)

def main():
    file_path = "input.txt"

    with open(file_path, 'r') as file:
        first_part, second_part = file.read().strip().split('\n\n')
        
        lines = first_part.split('\n')
        output_str_list = second_part.split('\n')

        output = [[int(num) for num in string.split(',')] for string in output_str_list]

        print_pages(lines, output)

if __name__ == "__main__":
    main()
