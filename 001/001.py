grid = [i for i in range(1, 10)]

def get_grid(grid):
    for i in range(3):
        print(grid[0 + i*3], '|', grid[1 + i*3], '|', grid[2 + i*3])
        print('-' * 10)

def take_input(player_token):
    value = False
    while not value:
        player_answer = input(f"Выбери номер клетки для {player_token}: ")
        try:
            player_answer = int(player_answer)
        except:
            print('Ошибка! Введите число от 1 до 9.')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(grid[player_answer - 1]) not in 'XO':
                grid[player_answer - 1] = player_token
                value = True
            else:
                print('Эта клетка занята!')
        else:
            print('Введите число от 1 до 9.')

def check_win(grid):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if grid[each[0]] == grid[each[1]] == grid[each[2]]:
            return grid[each[0]]
    return False

def main(grid):
    counter = 0
    win = False
    while not win:
        get_grid(grid)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(grid)
            if tmp:
                print(f'{tmp} выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    get_grid(grid)
main(grid)

input('Tap enter to exit...')
