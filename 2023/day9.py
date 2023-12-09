with open('day9_inputfile.txt') as file:
    my_input = [line.strip().split() for line in file.readlines()]


# Part 1
def find_next(num_lst):
    new_lst = []
    for i in range(len(num_lst) - 1):
        new_lst.append(num_lst[i+1] - num_lst[i])
    if [x for x in new_lst if x != 0]:
        return num_lst[-1] + find_next(new_lst)
    else:
        return num_lst[-1]


new = []
for line in my_input:
    new.append(find_next([int(x) for x in line]))
print(sum(new))


# Part 2
def find_previous(num_lst):
    new_lst = []
    for i in range(len(num_lst) - 1):
        new_lst.append(num_lst[i+1] - num_lst[i])
    if [x for x in new_lst if x != 0]:
        return num_lst[0] - find_previous(new_lst)
    else:
        return num_lst[0]


new = []
for line in my_input:
    new.append(find_previous([int(x) for x in line]))
print(sum(new))



