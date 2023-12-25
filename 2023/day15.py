from collections import defaultdict


def hash1(string):
    current_val = 0
    for char in string:
        current_val = (current_val + ord(char)) * 17 % 256
    return current_val


with open('day15_inputfile.txt') as file:
    my_input = file.readline().split(',')


def part1(my_input):
    total_val = 0
    for step in my_input:
        total_val += hash1(step)
    print(total_val)


def part2(my_input):
    boxes = defaultdict(lambda: {'labels': [], 'focal_lengths': []})
    for step in my_input:
        if step[-1] == '-':
            label = step[:-1]
            box = hash1(label)
            if label in boxes[box]['labels']:
                idx = boxes[box]['labels'].index(label)
                boxes[box]['labels'].pop(idx)
                boxes[box]['focal_lengths'].pop(idx)
        else:
            label = step[:-2]
            box = hash1(label)
            if label in boxes[box]['labels']:
                idx = boxes[box]['labels'].index(label)
                boxes[box]['focal_lengths'][idx] = step[-1]
            else:
                boxes[box]['focal_lengths'].append(step[-1])
                boxes[box]['labels'].append(label)

    total = 0
    for box_num, contents in boxes.items():
        for slot_num, lens in enumerate(contents['focal_lengths']):
            total += (1 + box_num) * (slot_num + 1) * int(lens)

    print(total)


part2(my_input)
