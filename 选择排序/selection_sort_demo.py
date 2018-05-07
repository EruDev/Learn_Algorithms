# coding: utf-8

def select_sort(alist):
	"""
	选择排序
	"""
	count = len(alist)
	for i in range(count):
		min_index = i
		for j in range(i + 1, count):
			if alist[j] < alist[i]:
				min_index = j

			alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [13, 42, 5, 23, 53, 24, 354]
select_sort(alist)
print(alist) 