# Pulling colorful cubes out of a bag

container = {'red': 12, 'green': 13, 'blue': 14}
valid_games = 0
total_power = 0

with open('day2_inputfile.txt') as file:
    for row in file:
        impossible = False
        minimum_cubes = {'red': 0, 'green': 0, 'blue': 0}
        game_input = row.split(':')
        game_ID = int(game_input[0].removeprefix('Game '))
        rounds = game_input[1].split(';')
        for round_info in rounds:
            cube_picks = round_info.split(', ')
            for color_picked in cube_picks:
                color_info = color_picked.split()
                if int(color_info[0]) > container[color_info[1]]:
                    impossible = True
                if int(color_info[0]) > minimum_cubes[color_info[1]]:
                    minimum_cubes[color_info[1]] = int(color_info[0])
        if not impossible:
            valid_games += game_ID
        power = 1
        for value in minimum_cubes.values():
            power *= value
        total_power += power

    print(f'valid_games: {valid_games}')
    print(f'total_power: {total_power}')
