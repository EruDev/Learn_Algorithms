# coding: utf-8

"""
有一个长度为n序列，移除掉里面的重复元素，对于每个相同的元素保留最后出现的那个

示例：

1,8,7,3,8,3,1

输出：

7,8,3,1
"""

def find_last(seq):
	li = list()
	for i in seq:
		if i not in li:
			li.append(i)
		else:
			li.remove(i)
			li.append(i)
	return li
	

if __name__ == '__main__':
	seq = [1, 1, 7, 1, 8, 3, 1, 7, 8] # 3,1,7,8
	print(find_last(seq))