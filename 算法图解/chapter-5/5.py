# coding: utf-8
"""
斐波那契数列: 又称黄金分割数列,
指得是这样一个数列, 1, 1, 2, 3, 5, 8...,
这个数列从第三项开始, 每一项都等于前两项之和。 求数列第n项
"""
# 我们很容易就可以写出这么一个递归函数
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)


li = fibonacci(5)
print(li)


# 改进一
def fibonacci(n, cache=None):
	if cache is None:
		cache = {}
	if n in cache:
		return cache[n]
	if n <= 1:
		return n
	cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
	return cache[n]

print(fibonacci(100))


# 改进二
def memo(func):
	cache = {}
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap

@memo
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(60))