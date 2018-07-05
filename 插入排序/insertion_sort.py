# coding: utf-8
def insertion_sort(seq):
	n = len(seq)
	for i in range(1, n):
		value = seq[i]
		pos = i
		while pos > 0 and value < seq[pos-1]:
			seq[pos] = seq[pos-1]
			pos -= 1
		seq[pos] = value
		print(seq)

import random

def test_insertion_sort():
	seq = list(range(10))
	random.shuffle(seq)
	insertion_sort(seq)


if __name__ == '__main__':
	test_insertion_sort()