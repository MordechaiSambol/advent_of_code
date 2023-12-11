# Start by checking if there are multiple ways for S to go, or just 2.
import re

with open('day10_inputfile.txt') as file:
    my_input = [row.strip() for row in file.readlines()]
    for i, row in enumerate(my_input):
        if 'S' in row:
            start_pos = (i, row.index('S'))
            break

next_dir = {'|': ((-1, 0), (1, 0)),
            '-': ((0, 1), (0, -1)),
            'L': ((0, 1), (-1, 0)),
            'J': ((0, -1), (-1, 0)),
            '7': ((0, -1), (1, 0)),
            'F': ((0, 1), (1, 0)),
            }

# Not really necessary because I know that the input is valid, just so pycharm stops marking things.
char = 'S'
pos = start_pos
last_step = (0, 0)

# Finding first direction from start
for delta in ((1, 0), (0, 1), (-1, 0), (0, -1)):
    if 0 <= start_pos[0] + delta[0] < len(my_input) and 0 <= start_pos[1] + delta[1] <= len(my_input[0]):
        pos = (start_pos[0] + delta[0], start_pos[1] + delta[1])
        char = my_input[pos[0]][pos[1]]
        if char in next_dir and (-delta[0], -delta[1]) in next_dir[char]:
            last_step = delta
            break

# Mapping out the path of the pipe
path = [start_pos, pos]
while char != 'S':
    for direction in next_dir[char]:
        if direction != (-last_step[0], -last_step[1]):
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            last_step = direction
            break
    path.append(pos)
    char = my_input[pos[0]][pos[1]]

# print(path)
print(f'Part 1 solution: {int(len(path) / 2)}')

# Part 2
non_path_pos = [(a, b) for a in range(len(my_input)) for b in range(len(my_input[0])) if (a, b) not in path]
# Replace all non_path_pos with a '.'
clean_input = [list(row) for row in my_input]
for pos in non_path_pos:
    clean_input[pos[0]][pos[1]] = '.'

# Replace 'S' with the appropriate marking
start_neighbor_pipes = {(path[1][0] - path[0][0], path[1][1] - path[0][1]),
                        (path[-1][0] - path[0][0], path[-1][1] - path[0][1])}
for pipe_type, directions in next_dir.items():
    if set(directions) == start_neighbor_pipes:
        clean_input[start_pos[0]][start_pos[1]] = pipe_type
        break

# Checking if a point is surrounded by the loop:
# If the loop passes on each side  of the point an uneven amount of times, then the point is surrounded by the loop.
# It's actually enough to check only on one side horizontally and on one side vertically.
# If each one of those is an uneven number, then there must be an uneven amount of passes on the opposite side too.
num_enclosed = 0
for pos in non_path_pos:  # Gotta be a good way to shorten this
    row = clean_input[pos[0]]
    on_right = ''.join(row[pos[1] + 1:])
    above = ''.join(clean_input[row_num][pos[1]] for row_num in range(pos[0]))
    if (len(re.findall(r'F-*J|L-*7|\|', on_right)) % 2 == 1
        and len(re.findall(r'F\|*J|7\|*L|-', above)) % 2 == 1
    ):
        num_enclosed += 1

    # TODO: Count in groups and not in singles. IF enclosed - all get added to enclosed. if not - first doesn't
    #  get added to enclosed, the rest are removed from non_path_pos.

print(f'Solution part 2: {num_enclosed}')
# print(clean_input)
