def greeting():
	print("Привет, пользователь!")

def get_name():
	name = input("Как тебя зовут")
	return name

def get_age():
	age = int(input("Сколько тебе лет"))
	return age

greeting()
name = get_name()
age = get_age()

print("Тебя зовут "+name+" и тебе "+str(age)+" лет")
