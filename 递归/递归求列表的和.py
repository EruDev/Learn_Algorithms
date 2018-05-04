# coding: utf-8
"""
基本思路:
基线条件, 如果列表中只有一个元素, 那么就返回这个元素
线性条件, 计算列表中除第一个元素外的其他数字的和, 将其再与第一个元素想加。 然后再返回
"""
def sum_array(arr):
	if len(arr) == 1:
		return sum(arr)
	else:
		return arr[0] + sum_array(arr[1:])

def sum(list): 
	if list == []: 
		return 0 
	return list[0] + sum(list[1:]) 

if __name__ == '__main__':
	arr = [2, 4, 6]
	# print(sum_array(arr))
	print(sum(arr))