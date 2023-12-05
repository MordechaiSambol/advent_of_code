# In the inputfile, make sure that there are *no* \n at the end. (Note that this is different from day5 part1)

# Explaining code: Each pair of seeds 79 14 represents a range(79, 79+14).
# In the code I called this a range, but actually had it saved as a tuple (start, end).
# Each a-to-b map in the input is a "transformation" - each original seed number is sent to a new number.
# The transformation is built of a set of rules which I saved in a dictionary: {source_range: destination_range}.
# I applied the first transformation on the original seeds by finding which parts of the seed ranges intersected the
# source_ranges of the transformation, and which didn't. Then I applied the second transformation on the results
# of the first one, and so on until the last transformation was done.

# So: 'with open' sets up the input - what is seeds and what are transformations.
# 'for transformation' iterates through the transformations - for each one it organizes the rules,
# and then applies them using 'apply_rules'. 'transform_range' does the transformation on a single range.


def apply_rules(trans_rules, ranges_to_trans):
    new_ranges = []
    for rule_in, rule_out in trans_rules.items():
        untransformed = []
        for range1 in ranges_to_trans:
            after_trans, still_untrans = transform_range(range1, rule_in, rule_out)
            new_ranges.extend(after_trans)
            untransformed.extend(still_untrans)
        ranges_to_trans = untransformed[:]
    new_ranges.extend(ranges_to_trans)
    return new_ranges[:]


def transform_range(range1, rule_in, rule_out):
    new_ranges = []
    remaining_ranges = []

    if range1[0] > rule_in[1] or range1[1] < rule_in[0]:
        remaining_ranges = [range1]
    else:
        left_diff = range1[0] - rule_in[0]
        right_diff = range1[1] - rule_in[1]

        # The overlap of range1 with rule_in
        new_ranges.append(
            (rule_out[0] + (left_diff if left_diff > 0 else 0), rule_out[1] + (right_diff if right_diff < 0 else 0))
        )
        # The parts of range1 that don't overlap with rule_in
        remaining_ranges.extend([
            (rule_in[1] + 1, range1[1]),
            (range1[0], rule_in[0] - 1)
        ])

    return new_ranges, [x for x in remaining_ranges if x[1] >= x[0]]


with open('day5_inputfile.txt') as file:
    seeds = file.readline().split()[1:]
    ranges_to_trans = []
    for i in range(0, len(seeds), 2):
        # Each of ranges_to_trans is in the form (start, end) where both are included.
        ranges_to_trans.append((int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1))
    file.readline()
    my_input = file.read().split('\n\n')

for transformation in my_input:
    # Setting up a dictionary where the keys are the source ranges, and the values are the destination ranges.
    trans_rules = {}
    trans_info = transformation.split('\n')[1:]
    for row in trans_info:
        rule = row.split()
        trans_rules[(int(rule[1]), int(rule[1]) + int(rule[2]) - 1)] = (int(rule[0]), int(rule[0]) + int(rule[2]) - 1)
    print(f'trans_rules: {trans_rules}')

    ranges_to_trans = apply_rules(trans_rules, ranges_to_trans)

print(min([x[0] for x in ranges_to_trans]))