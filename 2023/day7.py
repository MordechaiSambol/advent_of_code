def base_13_val(num_str):
    # For part 1
    # base_vals = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
    #              '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    # For part 2
    base_vals = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
                 '9': 8, 'T': 9, 'J': 0, 'Q': 10, 'K': 11, 'A': 12}

    value = 0
    for i, char in enumerate(num_str[::-1]):
        value += base_vals[char] * 13 ** i
    return value


def find_pattern(hand_str):
    histogram = [0]*13
    for char in hand_str:
        histogram[base_13_val(char)] += 1
    # For part 1
    # pattern = tuple(sorted((x for x in histogram if x > 0), reverse=True))
    # For part 2 {
    num_of_jokers = histogram[0]
    histogram[0] = 0
    if num_of_jokers == 5:
        pattern = (5, )
    else:
        pre_pattern = sorted((x for x in histogram if x > 0), reverse=True)
        pre_pattern[0] += num_of_jokers  # This is the best way to improve the hand
        pattern = tuple(pre_pattern)
    # }
    return pattern


with open('day7_inputfile.txt') as file:
    my_input = [hand.strip().split() for hand in file.readlines()]

patterns = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]  # Lowest to highest
hand_types = {pattern: [] for pattern in patterns}

for hand in my_input:
    pattern = find_pattern(hand[0])
    hand_types[pattern].append((base_13_val(hand[0]), int(hand[1])))
    # I replaced the hand with its value in base 13 for easier comparisons with the other hands of the same pattern.

ordered_hands = []
for pattern in patterns:
    ordered_hands.extend(sorted(hand_types[pattern], key=lambda x: x[0]))

total_wins = 0
for i, hand in enumerate(ordered_hands):
    total_wins += (i+1)*hand[1]

print(total_wins)
