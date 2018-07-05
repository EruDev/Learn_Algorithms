# coding: utf-8
import random

def select_sort(seq):
	n = len(seq)

	for i in range(n-1):
		min_idx = i
		for j in range(i+1, n):
			if seq[j] < seq[min_idx]:
				min_idx = j
			if min_idx != i:
				seq[i], seq[min_idx] = seq[min_idx], seq[i]
	print(seq)
	return min_idx

def test_select_sort():
	seq = list(range(10))
	random.shuffle(seq)
	min_idx = select_sort(seq)
	print(min_idx)


if __name__ == '__main__':
	test_select_sort()