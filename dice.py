import random

def d4(num=1):
	count = 0
	while num > 0 :
		count += random.randint(1,4)
		num-=1
	return count

def d6(num=1):
	count = 0
	while num > 0 :
		count += random.randint(1,6)
		num-=1
	return count

def d8(num=1):
	count = 0
	while num > 0 :
		count += random.randint(1,8)
		num-=1
	return count

def d10(num=1):
	count = 0
	while num > 0 :
		count += random.randint(1,10)
		num-=1
	return count

def d12(num=1):
	count = 0
	while num > 0 :
		count += random.randint(1,12)
		num-=1
	return count

def d20(num=1):
	count = 0
	while num > 0 :
		count += random.randint(1,20)
		num-=1
	return count

def main():
	print(d20())


if __name__ == '__main__':
	main()
