
with open('./day1_input.txt', 'r') as my_file:
    day1_input = [l.strip('\n') for l in my_file.readlines()]
calorie_list = []
sm = 0
for line in day1_input:
    if line.isnumeric():
        sm += int(line)
    else:
        calorie_list.append(sm)
        sm = 0
print(sum(sorted(calorie_list)[-3:]))
