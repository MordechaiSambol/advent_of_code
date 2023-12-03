# First and last digit/word-digit out of a string

with open('day1_inputfile.txt') as file:
    my_input = [line.strip() for line in file]

word_to_num = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}

calib_nums = []
for line in my_input:
    for word, num in word_to_num.items():
        line = line.replace(word, word[0] + num + word[-1])  # The word[0],word[-1] allow cases like twone to become 21.
    digits = [char for char in line if char.isnumeric()]
    calib_nums.append(int(digits[0] + digits[-1]))
print(sum(calib_nums))
