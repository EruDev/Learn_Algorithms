# coding: utf-8

def countdown(i):
	if i < 0:
		return
	else:
		countdown(i - 1)
		print(i)


if __name__ == '__main__':
	countdown(100)