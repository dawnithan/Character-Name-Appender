import string
import random

# len = input("how many extra chars: ")
name = input("name: ")
names = []
names_2 = []

common = ['a','e','i','o','u','n','r','n','s','l','t','g','d'] # 1 and 2
uncommon = ['m','b','p','y','f','v','w','h','k'] # 3, 4, and 5
rare = ['j','x','q','z'] # 8 and 10


def make_names_v1(name, names):
	for letter in range(random.randint(1,5)):
		letter = random.choice(string.ascii_lowercase)
		name += letter
	names.append(name)


def make_names_v2(name, names_2):
	for letter in range(random.randint(1,5)):
		roll = random.random()
		# print(roll)
		if (roll > 0.2):
			letter = random.choice(common)
		elif (roll <= 0.2 and roll > 0.1):
			letter = random.choice(uncommon)
		else:
			letter = random.choice(rare)
		name += letter
	names_2.append(name)


for times in range(10):
	make_names_v1(name, names)

for times in range(10):
	make_names_v2(name, names_2)

print("Using string.ascii_lowercase:")
print(names)
print("Using scrabble scoring:")
print(names_2)