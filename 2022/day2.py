with open('./day2_input.txt', 'r') as my_file:
    day2_input = my_file.read().split('\n')

total_score = 0
op_moves = 'ABC'
possible_outcomes = 'YZX'
for line in day2_input:
#     if op_moves.index(line[0]) == my_moves.index(line[2]):
#         outcome = 3
#     elif op_moves.index(line[0]) == (my_moves.index(line[2]) + 1) % 3:
#         outcome = 0
#     else:
#         outcome = 6
#     total_score += outcome + my_moves.index(line[2]) + 1

    outcome = ((possible_outcomes.index(line[2]) + 1) % 3) * 3
    my_play = (op_moves.index(line[0]) + possible_outcomes.index(line[2])) % 3 + 1
    total_score += outcome + my_play

print(total_score)