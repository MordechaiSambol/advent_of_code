with open('day3_input.txt', 'r') as input_file:
    input_info = input_file.read().split('\n')

# Part 1:
# wrong_items = []
# for rucksack in input_info:
#     comp1 = rucksack[:len(rucksack)//2]
#     comp2 = rucksack[len(rucksack)//2:]
#     for a in comp1:
#         if a in comp2:
#             # print(a)
#             if ord(a) > 96:
#                 new_mistake = ord(a) - 96
#             else:
#                 new_mistake = ord(a) - 38
#             wrong_items.append(new_mistake)
#             break


# Part 2:
wrong_items = []
for group in range(len(input_info)//3):
    elf1 = input_info[group*3]
    elf2 = input_info[group*3 + 1]
    elf3 = input_info[group*3 + 2]
    for a in elf1:
        if a in elf2 and a in elf3:
            if ord(a) > 96:
                new_mistake = ord(a) - 96
            else:
                new_mistake = ord(a) - 38
            wrong_items.append(new_mistake)
            break

# print(wrong_items)
print(sum(wrong_items))
