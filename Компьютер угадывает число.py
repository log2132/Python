import random

def guess (x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Угадайте число от 1 до {x}: '))
		if guess < random_number:
			print("Неверно, попробуй число больше")
		elif guess > random_number:
			print("Неверно, попробуй число меньше")

	print(f"Поздравляю,всё верно это было число {random_number}")



def computer_guess(x):

        low = 1
        high = x
        feedback = ""
        while feedback != 'c':
                if low != high:
                        guess = random.randint (low,high)
                else:
                        guess = low
                feedback = input (f'Is {guess}').lower()
                if feedback == 'l':
                        low = guess - 1
                elif feedback == 'h':
                        high = guess + 1 
        print(f'Ура Комьпютер смог угадать твоё число {guess}')


computer_guess(10)
