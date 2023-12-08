with open('day8_inputfile.txt') as file:
    # Turning series of steps into a string of 0's and 1's - 0 means 'L' and 1 means 'R'.
    steps = file.readline().strip().replace('L', '0').replace('R', '1')
    file.readline()  # Passes over the empty line
    # Creating a dictionary with, for example: {'AAA': ('XHV', 'KDJ')}
    nodes = {}
    for node in file.readlines():
        node_info = node.split(' = ')
        nodes[node_info[0]] = tuple(node_info[1].removeprefix('(').removesuffix(')\n').split(', '))

steps_taken = 0
next_step = 'AAA'
next_direction_index = 0
while next_step != 'ZZZ':
    if next_direction_index >= len(steps):
        next_direction_index = 0
    next_step = nodes[next_step][int(steps[next_direction_index])]
    steps_taken += 1
    next_direction_index += 1

print(steps_taken)
