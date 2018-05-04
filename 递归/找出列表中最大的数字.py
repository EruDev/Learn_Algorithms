# coding: utf-8

def max(arr):
	max_num = 0
	index = 0
	for i in arr:
		if i > arr[index]:
			max_num = i
	return max_num


if __name__ == '__main__':
	print(max([1, 32, 3, 53, 532]))