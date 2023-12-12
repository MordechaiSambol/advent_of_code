# Change this var for part 1 or part 2
expansion = 1000000


def transpose(mat):
    new_mat = []
    for col_num in range(len(mat[0])):
        new_mat.append([row[col_num] for row in mat])
    return new_mat


with open('day11_inputfile.txt') as file:
    my_input = [row.strip() for row in file.readlines()]

empty_rows = []
empty_cols = []
for lst, mat in zip([empty_rows, empty_cols], [my_input, transpose(my_input)]):
    for row_num, row in enumerate(mat):
        if '#' not in row:
            lst.append(row_num)

galaxy_pos = []
pos = [0, 0]
for row_num, row in enumerate(my_input):
    pos[1] = 0
    for col_num, val in enumerate(row):
        if val == '#':
            galaxy_pos.append(tuple(pos))
        pos[1] += expansion if col_num in empty_cols else 1
    pos[0] += expansion if row_num in empty_rows else 1

path_sum = 0
for i, galaxy in enumerate(galaxy_pos):
    for other_gal in galaxy_pos[i + 1:]:
        path_sum += abs(other_gal[0] - galaxy[0]) + abs(other_gal[1] - galaxy[1])

print(path_sum)
