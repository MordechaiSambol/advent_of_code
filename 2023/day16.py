with open('day16_inputfile.txt') as file:
    my_input = [[x for x in row.strip()] for row in file.readlines()]

special_char = {'|': ((-1, 0), (1, 0)),
                '-': ((0, 1), (0, -1)),
                'L': ((0, 1), (-1, 0)),
                'J': ((0, -1), (-1, 0)),
                '7': ((0, -1), (1, 0)),
                'F': ((0, 1), (1, 0)),
                }

dir_arrows = {(0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'}


def count_energized(my_input, path, special_char, dir_arrows):
    length = len(my_input)
    width = len(my_input[0])
    lit_tiles = 0
    next_char = '.'

    for pos in path:
        row, col = pos[0]
        row_delta, col_delta = pos[1]
        next_pos = (row + row_delta, col + col_delta)
        reverse_dir = (-row_delta, -col_delta)

        if 0 <= next_pos[0] < length and 0 <= next_pos[1] < width:
            next_char = my_input[next_pos[0]][next_pos[1]]
            replacement_char = next_char

            # Continuing straight
            if next_char == '.' or next_char in '<>^v'.replace(dir_arrows[reverse_dir], ''):
                path.append((next_pos, pos[1]))
                replacement_char = dir_arrows[pos[1]] if next_char == '.' else 'X'

            # Hit a special character that's not a mirror
            elif next_char in '|-' or (next_char in 'L7JF' and reverse_dir in special_char[next_char]):
                for direction in special_char[next_char]:
                    if direction != reverse_dir:
                        path.append((next_pos, direction))
                replacement_char = 'X'

            # Hit a mirror
            elif next_char in r'\/':
                mirror_type = r'\/'.index(next_char)
                mirror_factor = (-1)**mirror_type
                path.append((next_pos, (mirror_factor*col_delta, mirror_factor*row_delta)))
                # Switching mirror with L7JF to represent the side of the mirror that wasn't hit yet.
                replacement_char = 'L7JF'[2*mirror_type + (row_delta > 0 or col_delta*mirror_factor < 0)]

            if next_char in r'.\/|-':
                lit_tiles += 1

            my_input[next_pos[0]][next_pos[1]] = replacement_char
    return lit_tiles


length = len(my_input)
width = len(my_input[0])
starting_places = []
for row_num in range(length):
    starting_places.append(((row_num, -1), (0, 1)))  # (row, col), (direction_moving)
    starting_places.append(((row_num, width), (0, -1)))
for col_num in range(width):
    starting_places.append(((-1, col_num), (1, 0)))
    starting_places.append(((length, col_num), (-1, 0)))

scores = []
for start in starting_places:
    input_copy = [[char for char in row] for row in my_input]
    scores.append(count_energized(input_copy, [start], special_char, dir_arrows))

print(max(scores))
