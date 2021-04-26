import random, string

def generate_password(lenght=16, inc_symbols=False, inc_numbers=True, inc_lowercase=True, inc_uppercase=True, inc_similar=True):
	symbols = string.punctuation
	numbers = string.digits
	lower_letters = string.ascii_lowercase
	upper_letters = string.ascii_uppercase

	pos_letters = []
	new_password = []

	if inc_symbols:
		pos_letters += symbols

	if inc_numbers:
		pos_letters += numbers

	if inc_lowercase:
		pos_letters += lower_letters

	if inc_uppercase:
		pos_letters += upper_letters

	if inc_similar:
		while len(new_password) < lenght:
			new_password += random.choice(pos_letters)
	else:
		new_password = set(new_password)
		while len(new_password) < lenght:
			new_password.add(random.choice(pos_letters))


	return ''.join(new_password)


for _ in range(10):
	password = generate_password(lenght=random.randint(8, 32), inc_symbols=random.choice([True, False]), inc_numbers=random.choice([True, False]), inc_lowercase=True, inc_uppercase=random.choice([True, False]), inc_similar=random.choice([True, False]))
	print(password)