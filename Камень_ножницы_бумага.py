import random

def play():
    User = input ("Сделай свой выбор 'Камень''Бумага''Ножницы'\n")
    computer = random.choice(['Камень','Бумага','Ножницы'])
    #в случае нечьей
    if user == computer:
        return 'Нечья\'4'
    # в случае победы
    if is_win(user, computer):
        return 'ТЫ ВЫЙГРАЛ'
    return 'ТЫ ПРОИГРАЛ'

def is_win(player, opponent):
    # в случае проигрыша
    if (player == 'Камень' and opponent == 'Ножницы') or (player == 'Ножницы' and opponent == 'Бумага') or (player == 'Бумага' and opponent == 'Камень'):
        return True
