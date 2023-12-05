# In the inputfile, make sure that there are *no* \n at the end.
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

    if rule_in[0] <= range1[0] <= rule_in[1] <= range1[1]:
        diff = range1[0] - rule_in[0]
        new_ranges.append((rule_out[0] + diff, rule_out[1]))
        if rule_in[1] < range1[1]:
            remaining_ranges.append((rule_in[1] + 1, range1[1]))

    elif range1[0] <= rule_in[0] <= range1[1] <= rule_in[1]:
        diff = range1[1] - rule_in[0]
        new_ranges.append((rule_out[0], rule_out[0] + diff))
        if range1[0] < rule_in[0]:
            remaining_ranges.append((range1[0], rule_in[0] - 1))

    elif rule_in[0] <= range1[0] <= range1[1] <= rule_in[1]:
        diff = range1[0] - rule_in[0]
        new_ranges.append((rule_out[0] + diff, rule_out[0] + diff + range1[1] - range1[0]))

    else:
        remaining_ranges = [range1]

    return new_ranges, remaining_ranges


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
