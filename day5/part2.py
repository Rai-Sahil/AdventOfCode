import collections

def fix_order(order, adj):
    ordered_output = []

    # Step 1: Start by adding courses that don't have any prerequisites (these can appear first)
    while len(order) > 0:
        for page in order:
            # Iterate on each page in order. If that page as any before-page
            # and that page is in order already,
            # go to add until you get to a page that doesn't have before-page
            # and that page i not in order.
            # Add that. Follow the same shit until you get to empty order list.
            # PS: Let's say we get to a page whose prereq is already in order.
            # DW the loop will get to it naother time, once it's done with next
            # page in order list. Do remove page from order list cuz it's
            # already processed (added) but loop will iterate over it again if
            # not removed.
            if all(prereq not in order for prereq in adj[page]):
                ordered_output.append(page)
                order.remove(page)
                break

    return ordered_output

def print_pages(pages, outputs):
    adj = collections.defaultdict(list)
    incorrect_orders = []
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

            if not found:
                incorrect_orders.append(output)
                break
    
    for order in incorrect_orders:
        fixed_order = fix_order(order, adj)
        middle_index = len(fixed_order) // 2
        
        sum += fixed_order[middle_index]

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

