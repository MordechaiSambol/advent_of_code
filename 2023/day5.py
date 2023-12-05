# In the inputfile, make sure that there are two \n at the end (so press enter twice).
# That's necessary for the regex I used.

import re

with open('day5_inputfile.txt') as file:
    seeds = set(re.findall(r'\d+', file.readline()))
    map_input = file.read()

maps_info = []
for map_subject in re.findall(r':\n([\d|\n| ]+)\n{2}', map_input):
    subject_info = []
    for single_map in map_subject.split('\n'):
        single_map_info = single_map.split()
        subject_info.append(
            {'destination_start': int(single_map_info[0]),
             'source_start': int(single_map_info[1]),
             'range_length': int(single_map_info[2])
             }
        )
    maps_info.append(subject_info)

# maps_info = [[{'source_start': int(single_map.split()[0]),
#                'destination_start': int(single_map.split()[1]),
#                'range_length': int(single_map.split()[2])
#                }
#               for single_map in map_subject.split('\n')
#               ]
#              for map_subject in re.findall(r':\n([\d|\n| ]+)\n{2}', map_input)
#              ]


def next_step(piece, subject_num):
    for single_map in maps_info[subject_num]:
        diff = int(piece) - single_map['source_start']
        if 0 <= diff < single_map['range_length']:
            return single_map['destination_start'] + diff
    return int(piece)


for subject in range(len(maps_info)):
    seeds = set(map(next_step, seeds, [subject]*len(seeds)))

print(min(seeds))
