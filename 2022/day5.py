with open('day5_input.txt', 'r') as input_file:
    input_info = input_file.read().split('\n')
# Turning each stack of crates into a list of crates, where the first crate in each list is the top crate
# in the stack.
stack_info = ['']*9
for line in input_info[:8]:
    line = line.replace('    ', ' [0] ').split() # Replaces "holes" when some stacks are taller than others.
    # print(f'line: {line}')
    for stack, crate in enumerate(line):
        if crate != '[0]':
            stack_info[stack] += crate[1]
# print(stack_info)

# Moving crates from one stack to the other
for line in input_info[10:]:
    move_info = line.split()
    num_of_crates = int(move_info[1])
    origin_stack = int(move_info[3]) - 1
    goal_stack = int(move_info[5]) - 1
    crates_moved = stack_info[origin_stack][:num_of_crates]
    stack_info[goal_stack] = crates_moved + stack_info[goal_stack]
    stack_info[origin_stack] = stack_info[origin_stack][num_of_crates:]

top_crates = [stack[0] for stack in stack_info]
# print(stack_info)
print(''.join(top_crates))
