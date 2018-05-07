# coding: utf-8

# def bubble_sort(alist):
# 	"""
# 	冒泡排序, 时间复杂度为 O(n^2)
# 	"""
# 	for i in range(len(alist)-1, 0, -1):
# 		for j in range(i):
# 			if alist[j] > alist[j+1]:
# 				alist[j], alist[j+1] = alist[j+1], alist[j]


# li = [3, 432, 42, 23, 34, 1]
# bubble_sort(li)
# print(li)

def bubble_sort(alist):
	count = len(alist)
	for i in range(count):
		for j in range(i + 1, count):
			if alist[i] > alist[j]:
				alist[i], alist[j] = alist[j], alist[i]


li = [3, 432, 42, 23, 34, 1]
bubble_sort(li)
print(li)