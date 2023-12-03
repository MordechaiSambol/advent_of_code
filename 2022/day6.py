with open('day6_input.txt', 'r') as input_file:
    input_info = input_file.read()
for i in range(len(input_info) - 13):
    same = 0
    for letter in input_info[i:i+14]:
        remaining_letters_list = list(input_info[i:i+14])
        remaining_letters_list.remove(letter)
        if letter in remaining_letters_list:
            same = 1
            break
    if same == 0:
        print(input_info[i:i+14])
        print(i+14)
        break
