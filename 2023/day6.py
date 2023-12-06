import re, math

with open('day6_inputfile.txt') as file:
    # Part 1
    times = [int(x) for x in re.split(r'\s+', file.readline().strip())[1:]]
    distances = [int(x) for x in re.split(r'\s+', file.readline().strip())[1:]]
    # For Part 2 replace with the following
    # times = [int(''.join(re.split(r'\s+', file.readline().strip())[1:]))]
    # distances = [int(''.join(re.split(r'\s+', file.readline().strip())[1:]))]

result = 1
for time1, distance1 in zip(times, distances):
    lower_boundry = (time1 - math.sqrt(time1 ** 2 - 4 * distance1)) / 2
    upper_boundry = (time1 + math.sqrt(time1 ** 2 - 4 * distance1)) / 2
    result *= (math.floor(upper_boundry) - math.ceil(lower_boundry) + 1
               - 1 * (upper_boundry % 1 == 0) - 1 * (lower_boundry % 1 == 0))

print(result)
