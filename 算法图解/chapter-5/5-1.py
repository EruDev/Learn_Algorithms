# coding:utf-8

"""
看完第四章的分治法后我们来做一道leetcode 题

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

def maxList(nums):
	max_num = nums[0]
	n = len(nums)
	li = []
	li.append(max_num)
	for i in range(1, n):
		li.append(nums[i])

		if li[i-1] > 0:
			li[i] = li[i] + li[i-1]
		if li[i] > max_num:
			max_num = li[i]
	return max_num
		
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxList(nums))