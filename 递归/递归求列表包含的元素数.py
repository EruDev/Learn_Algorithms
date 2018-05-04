# coding: utf-8

"""
基线条件, 如果是空列表, 就返回0
线性条件, 计算列表除第一个元素外的其他元素的个数和, 然后再加上 1返回
"""
def count(arr):
	if arr == []:
		return 0
	return 1 + count(arr[1:])


if __name__ == '__main__':
	print(count([x for x in range(10)]))