with open('day8_inputfile.txt') as file:
    # Turning series of steps into a string of 0's and 1's - 0 means 'L' and 1 means 'R'.
    steps = file.readline().strip().replace('L', '0').replace('R', '1')
    file.readline()  # Passes over the empty line
    # Creating a dictionary with, for example: {'AAA': ('XHV', 'KDJ')}
    nodes = {}
    for node in file.readlines():
        node_info = node.split(' = ')
        nodes[node_info[0]] = tuple(node_info[1].strip().removeprefix('(').removesuffix(')').split(', '))

# Creating a dictionary with, for example: {'AAA': ('BBB', {283})}
# The key is the starting node, value[0] is the next node if we take all the steps in our steps input once,
# value[1] is a set of how many steps are between 'AAA' and the following nodes that end with Z.
# After one run I realized that the nodes that end with Z will always be reached at the end of a steps cycle.
# For that reason, value[1] will always be an empty set or {283}, so I took it out.
node_names = [node for node in nodes]
steps_from_node = {}
for node in node_names:
    steps_taken = 0
    next_step = node
    steps_to_z = set()
    for direction_str in steps:
        next_step = nodes[next_step][int(direction_str)]
        steps_taken += 1
        if next_step[-1] == 'Z':
            steps_to_z.add(steps_taken)
    steps_from_node[node] = [next_step]


# First - Finding loops:
starting_pos = [node for node in node_names if node[-1] == 'A']
for node in starting_pos:
    path = [node]
    next_node = steps_from_node[node][0]
    while next_node not in path:
        path.append(next_node)
        next_node = steps_from_node[next_node][0]
    loop_start_i = path.index(next_node)
    loop = path[loop_start_i:]
    num_steps_before_loop = loop_start_i
    print(f'node: {node} path: {path}')
    print(f'loop: {loop}')

    # Finding Zs in loop
    z_pos = []
    for i, loop_node in enumerate(loop):
        if loop_node[-1] == 'Z':
            z_pos.append(i)

    steps_from_node[node].extend([len(loop), z_pos, num_steps_before_loop])
    # So now steps_from_node is of shape: {'AAA': ['BBB', 5, [0, 2, 3], 4]} (For the starting_pos anyway).

print([x for x in steps_from_node.items() if len(x[1]) > 1])

# After mapping out the loops, it turns out that every starting position takes one step and then enters a loop at the
# start. There's only one end in each loop, and it always at the end of the loop. So effectively it's as if each ghost
# starts at an end point, and has to go through the whole loop to get back to it. Then it's only a question of finding
# the smallest number that's a multiple of the lengths of all the loops.
# For a more general solution, I could have used more math - to find when the first ghost reaches a z.
# Then use multiples of the length of his loop, to get the second ghost closer and closer to his z.
# Then multiples of both those loops, Until the third ghost gets to his z.
# And so on. I worked out with Aharon all the different possibilities in order to create a general solution,
# but that would need a lot of code that I'm not going to write right now.
