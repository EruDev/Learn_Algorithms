# coding: utf-8

"""
基本思路:
要对一个列表进行排序,
可以先找到一个基准点,
然后小于基准的分为一个组,
大于基准的分为一个组, 
然后将它们相加返回
"""
def quick_sort(seq):
	if len(seq) < 2:
		return seq
	else:
		pivot_index = 0
		pivot = seq[pivot_index]
		less_part = [i for i in seq[pivot_index+1:] if i <= pivot]
		great_part = [i for i in seq[pivot_index+1:] if i > pivot]

	return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort(seq):
	import random
	seq = list(range(10))
	random.shuffle(seq)
	quick_sort(seq)


if __name__ == '__main__':
	test_quick_sort()