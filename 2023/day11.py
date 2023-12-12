def expand_vertically(mat):
    new_mat = []
    for row in mat:
        new_mat.append(row)
        if '#' not in row:
            new_mat.append(row)
    return new_mat


def transpose(mat):
    new_mat = []
    for col_num in range(len(mat[0])):
        new_mat.append([row[col_num] for row in mat])
    return new_mat


with open('day11_inputfile.txt') as file:
    my_input = [row.strip() for row in file.readlines()]

my_input = expand_vertically(my_input)
my_input = transpose(my_input)
my_input = expand_vertically(my_input)

galaxy_pos = []
for row_num, row in enumerate(my_input):
    for col_num, val in enumerate(row):
        if val == '#':
            galaxy_pos.append((row_num, col_num))

path_sum = 0
for i, galaxy in enumerate(galaxy_pos):
    for other_gal in galaxy_pos[i + 1:]:
        path_sum += abs(other_gal[0] - galaxy[0]) + abs(other_gal[1] - galaxy[1])

print(path_sum)
