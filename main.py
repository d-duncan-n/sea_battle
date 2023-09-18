import random

def create_board():
    board = []
    for _ in range(10):
        row = ["O"] * 10
        board.append(row)
    return board

# Выводим игровое поле на экран
def print_board(board):
    for row in board:
        print(" ".join(row))

# Размещаем корабли на поле
def place_ships(board):
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # Длины кораблей
    for ship_length in ships:
        while True:
            orientation = random.choice(["horizontal", "vertical"])
            if orientation == "horizontal":
                x = random.randint(0, 9)
                y = random.randint(0, 9 - ship_length)
            else:
                x = random.randint(0, 9 - ship_length)
                y = random.randint(0, 9)
            if is_valid_placement(board, ship_length, x, y, orientation):
                place_ship(board, ship_length, x, y, orientation)
                break

# Проверяем, можно ли разместить корабль на данной позиции
def is_valid_placement(board, ship_length, x, y, orientation):
    if orientation == "horizontal":
        for i in range(ship_length):
            if board[x][y + i] != "O":
                return False
    else:
        for i in range(ship_length):
            if board[x + i][y] != "O":
                return False
    return True

# Размещаем корабль на поле
def place_ship(board, ship_length, x, y, orientation):
    if orientation == "horizontal":
        for i in range(ship_length):
            board[x][y + i] = "S"
    else:
        for i in range(ship_length):
            board[x + i][y] = "S"

# Выстрел игрока
def player_shot(board):
    while True:
        try:
            x = int(input("Введите номер строки (0-9): "))
            y = int(input("Введите номер столбца (0-9): "))
            if 0 <= x < 10 and 0 <= y < 10:
                if board[x][y] == "S":
                    print("Попадание!")
                    board[x][y] = "X"
                    return
                elif board[x][y] == "X" or board[x][y] == "M":
                    print("Вы уже стреляли в эту клетку.")
                else:
                    print("Мимо!")
                    board[x][y] = "M"
                    return
            else:
                print("Неверные координаты. Введите числа от 0 до 9.")
        except ValueError:
            print("Введите корректные числа.")

# Выстрел компьютера
def computer_shot(board):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if board[x][y] == "S":
            print("Компьютер попал в ваш корабль!")
            board[x][y] = "X"
            return
        elif board[x][y] == "X" or board[x][y] == "M":
            continue
        else:
            print("Компьютер промахнулся!")
            board[x][y] = "M"
            return

# Проверяем, закончена ли игра
def is_game_over(board):
    for row in board:
        if "S" in row:
            return False
    return True

# Основная функция игры
def main():
    player_board = create_board()
    computer_board = create_board()

    print("Добро пожаловать в игру 'Морской бой'!")
    print("Ваше поле:")
    print_board(player_board)
    print("")

    place_ships(player_board)
    place_ships(computer_board)

    while True:
        print("Ваш ход:")
        player_shot(computer_board)
        print_board(computer_board)
        if is_game_over(computer_board):
            print("Вы победили! Поздравляем!")
            break

        print("\nХод компьютера:")
        computer_shot(player_board)
        print_board(player_board)
        if is_game_over(player_board):
            print("Компьютер победил. Попробуйте еще раз.")
            break

if __name__ == "__main__":
    main()