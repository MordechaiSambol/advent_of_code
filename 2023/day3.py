import re
from collections import defaultdict

with open('day3_inputfile.txt') as file:
    my_input = [line.strip() for line in file]


# Given a row_num and placement=(start, end+1), returns a list of all the neighboring coordinates (including diagonals)
def find_neighbors(row_num, placement, height, width):
    neighbors = []
    for row in range(row_num - 1, row_num + 2):
        if 0 <= row < height:
            for col in range(placement[0] - 1, placement[1] + 1):
                if 0 <= col < width and not (row == row_num and placement[0] <= col < placement[1]):
                    neighbors.append((row, col))
    return neighbors


def near_symbol(neighbors, all_input, gear_dict, num_value):
    is_part_num = False

    for neighbor in neighbors:
        neighbor_value = all_input[neighbor[0]][neighbor[1]]
        if not neighbor_value.isnumeric() and neighbor_value != '.':
            is_part_num = True
            if neighbor_value == '*':
                gear_dict[neighbor].append(num_value)

    return is_part_num


part_num_sum = 0
gear_dict = defaultdict(lambda: [])
for row_num, row in enumerate(my_input):
    nums = [obj for obj in re.finditer(r'\d+', row)]
    for num_obj in nums:
        neighbors = find_neighbors(row_num, num_obj.span(), len(my_input), len(my_input[0]))
        if near_symbol(neighbors, my_input, gear_dict, int(num_obj.group(0))):
            part_num_sum += int(num_obj.group(0))
print(f'Sum of part numbers is: {part_num_sum}')

gear_ratios = 0
for lst in gear_dict.values():
    if len(lst) == 2:
        gear_ratios += lst[0]*lst[1]
print(f'Sum of gear ratios is: {gear_ratios}')
