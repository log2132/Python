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

guess(15)
		
