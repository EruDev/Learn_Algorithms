# coding: utf-8

def fact(num):
	if num == 1:
		return 1
	else:
		return num * fact(num - 1)

if __name__ == '__main__':
	print(fact(5))