# coding: utf-8
"""
给定一个有序（非降序）数组A，可含有重复元素，求最小的i使得A[i]等于target，不存在则返回-1。
时间复杂度要求为：O(logn)
"""
# def binarySearch(list, item):
# 	low = 0
# 	high = len(list) - 1
# 	while low <= high:
# 		mid = (high + low) // 2
# 		guess = list[mid]
# 		if guess == item:
# 			return mid
# 		if guess > item:
# 			high = mid - 1
# 		else:
# 			low = mid + 1
# 	return - 1


# if __name__ == '__main__':
# 	li = [1, 3, 5, 7, 9]
# 	print(binarySearch(li, 3))
# 	print(binarySearch(li, 10))

def binarySearch(list, item):
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = (high + low) // 2
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid -1
		else:
			low = mid + 1
	return -1

if __name__ == '__main__':
	li = [1, 3, 5, 7, 9]
	print(binarySearch(li, 3))   # 1
	print(binarySearch(li, 10)) # -1