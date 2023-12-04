import re

with open('day4_inputfile.txt') as file:
    my_input = [line.strip() for line in file]


def score_card(card):
    matches = 0
    card_info = re.sub(r'\s{2,}', ' ', card).split(' | ')
    card_info[0] = re.sub(r'Card \d+: ', '', card_info[0])
    win_nums, my_nums = card_info[0].split(), card_info[1].split()
    for num in my_nums:
        if num in win_nums:
            matches += 1
    return matches


card_multiples = {card_num: 1 for card_num in range(1, len(my_input) + 1)}
total = 0
for card_num, card in zip(range(1, len(my_input) + 1), my_input):
    points = score_card(card)
    if points > 0:
        total += 2**(points - 1)
        for card_won_delta in range(1, points+1):
            if card_num + card_won_delta <= len(my_input):
                card_multiples[card_num + card_won_delta] += card_multiples[card_num]

total_cards_won = 0
for cards in card_multiples.values():
    total_cards_won += cards

print(f'total: {total}')
print(f'total cards won: {total_cards_won}')
