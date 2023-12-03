def create_elf_list(pair):
    elf_list = pair.split(',')
    for i, elf in enumerate(elf_list):
        elf_list[i] = elf.split('-')
    # print(elf_list)
    return elf_list


def contained_check(pair):
    elf_list = create_elf_list(pair)
    if (int(elf_list[0][0]) >= int(elf_list[1][0]) and int(elf_list[0][1]) <= int(elf_list[1][1])
            or int(elf_list[0][0]) <= int(elf_list[1][0]) and int(elf_list[0][1]) >= int(elf_list[1][1])):
        # print('contained!')
        return 1
    return 0


def overlapping_check(pair):
    elf_list = create_elf_list(pair)
    if (int(elf_list[1][0]) <= int(elf_list[0][0]) <= int(elf_list[1][1])
            or int(elf_list[1][0]) <= int(elf_list[0][1]) <= int(elf_list[1][1])
            or contained_check(pair)):
        # print('overlapping!')
        return 1
    return 0


with open('day6_input.txt', 'r') as input_file:
    input_info = input_file.read().split('\n')
contained = 0
overlapping = 0
for pair in input_info:
    # print(pair)
    contained += contained_check(pair)
    overlapping += overlapping_check(pair)
print(f'contained: {contained}')
print(f'overlapping: {overlapping}')
