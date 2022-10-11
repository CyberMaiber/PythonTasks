# 3. Создайте программу для игры в 'Крестики-нолики'.

# Начальное игровое поле
field = [1,2,3,4,5,6,7,8,9]

#список списков выигрышных комбинаций
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Вывод игрового поля на экран
def print_field():
    print ("-------------")
    print("| " + str(field[0]), end = " | ")
    print(str(field[1]), end = " | ")
    print(str(field[2]) + " |")
    print ("|-----------|")
    print("| " + str(field[3]), end = " | ")
    print(str(field[4]), end = " | ")
    print(str(field[5]) + " |")
    print ("|-----------|")
    print("| " + str(field[6]), end = " | ")
    print(str(field[7]), end = " | ")
    print(str(field[8]) + " |")
    print ("-------------")
 
# Сделать ход
def step_field(step,sybm):
    ind = field.index(step)
    field[ind] = sybm
 
# Получить результат игры
def get_result():
    win = ""
    for i in wins: #перебор всех элементов списке списков wins
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":win = "O"       
    return win
 
# Тело программы
game_over = False
player1 = True
while not game_over:
    print_field()
    # Просим делать ход
    if player1:
        sybm = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        sybm = "O"
        step = int(input("Игрок 2, ваш ход: "))
    step_field(step,sybm) # делаем ход в указанную клетку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1) #переход хода       
# гамовер      
print_field()
print("Победил Игрок 1 (X)" if win == "X" else "Победил Игрок 2 (O)")