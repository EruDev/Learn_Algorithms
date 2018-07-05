# coding: utf-8
# 冒泡排序
import random

def bubble_sort(seq):
	n = len(seq)
	for i in range(n-1):
		for j in range(n-1-i):
			if seq[j] > seq[j+1]:
				seq[j], seq[j+1] = seq[j+1], seq[j]
	print(seq)


def test_bubble_sort():
	seq = list(range(10))
	random.shuffle(seq)  # 打扰数组
	bubble_sort(seq)


if __name__ == '__main__':
	test_bubble_sort()