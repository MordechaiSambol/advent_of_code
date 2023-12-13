import re


def fit(springs, group):
    matches = 0
    for i in range(len(springs) - sum(group) - (len(group) - 1)):
        end_check = len(springs) if len(group) == 1 else i + group[0] + 1
        if '.' not in springs[i:i + group[0]] and '#' not in springs[i + group[0]:end_check]:
            matches += 1 if len(group) == 1 else fit(springs[i + group[0] + 1:], group[1:])
        if springs[i] == '#':
            break
    return matches


def fit2(springs, groups, group_ints):
    if len(groups) == 1:
        pattern = '(?=' + groups[0] + '(?!.*#.*))'
    else:
        pattern = '(?=' + groups[0] + '(?=[.|?]+' + '[.|?]+'.join(groups[1:]) + '[.|?]*$))'

    last_idx_to_check = len(springs) if '#' not in springs else springs.index('#')
    # print([match for match in re.finditer(pattern, springs)])
    matches = [match for match in re.finditer(pattern, springs) if match.span()[0] <= last_idx_to_check
               and (match.span()[1] + group_ints[0] >= len(springs) or springs[match.span()[1] + group_ints[0]] != '#')]
    # print(matches)

    if len(groups) == 1:
        return len(matches)
    else:
        num_matches = 0
        for match in matches:
            num_matches += fit2(springs[match.span()[1] + group_ints[0] + 1:], groups[1:], group_ints[1:])
        return num_matches


with open('day12_inputfile.txt') as file:
    my_input = file.readlines()

# b = []
total = 0
for line in my_input:
    # print(f'now doing line: {line}')
    line_info = line.split()
    # Part 1
    # springs = line_info[0]
    # groups = ['[#|?]{' + num + '}' for num in line_info[1].split(',')]

    # Part 2
    springs = '?'.join([line_info[0]]*5)  # Part 2
    groups = ['[#|?]{' + num + '}' for num in ((line_info[1] + ',')*5).split(',')[:-1]]
    # print(springs)
    # print(groups)
    a = fit2(springs, groups, [int(x) for x in ((line_info[1] + ',')*5).split(',')[:-1]])
    print(a)
    total += a

    # b.append(fit(line.split()[0] + '.', [int(x) for x in line.split()[1].split(',')]))
    # if b[-1] != a:
    #     print(f'now doing line: {line}')
    #     print(f'regex version: {a}, original version: {b[-1]}')

print(total)









# with open('day12_inputfile.txt') as file:
#     my_input = file.readlines()
#
# b = []
# for line in my_input:
#     b.append(fit(line.split()[0] + '.', [int(x) for x in line.split()[1].split(',')]))
#     # print('.')
# # a = [fit(line.split()[0] + '.', [int(x) for x in line.split()[1].split(',')]) for line in my_input]
# # print(a)
# total_options = sum(b)
# print(total_options)
