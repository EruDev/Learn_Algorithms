# coding: utf-8

# 选择排序
def find_smallest(arr):
	small_index = 0
	small = arr[0]
	for i in range(1, len(arr)):
		if arr[i] < small:
			small_index = i
			small = arr[i]
	return small_index


if __name__ == '__main__':
	li = [42, 43, 64, 7, 5]
	print(find_smallest(li))