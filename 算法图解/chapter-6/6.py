# coding: utf-8

"""
这是书中芒果销售商问题
名字结尾是 `m` 代表是销售商
"""
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
	search_deque = deque()
	search_deque += graph[name]
	searched = []
	while searched:
		person = search_deque.popleft()
		if person is not searched:
			if person_is_seller(person):
				print('Person' + person + 'is a mango seller')
				return True
			else:
				search_deque += graph[person]
				searched.append(person)
	return False

def person_is_seller(name):
	return name[-1] == 'm'

print(search('you'))