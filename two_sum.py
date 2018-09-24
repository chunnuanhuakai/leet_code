# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:47:19 2018

@author: liuHongBing
"""

'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
'''
a = [3,10,9,2,4]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if target%2==0:
        ind = [i for i in range(len(nums)) if nums[i]==target//2 ]
        if len(ind)>=2:
            return ind[0:2]
        
    nums2= [target-i for i in nums]
    numsset = set(nums)
    nums2set = set(nums2)
    filterset = set()
    if target%2==0:
        filterset.add(target//2)
    
    
    value = list((numsset & nums2set) - filterset)
    index = [i for i in range(len(nums)) if nums[i] in value ]

    return index 


def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if target%2==0:
        ind = [i for i in range(len(nums)) if nums[i]==target//2 ]
        if len(ind)>=2:
            return ind[0:2]
        
    nums2= [target-i for i in nums]
    filterset = set()
    if target%2==0:
        filterset.add(target//2)
    value = [ind for ind in nums2 if (ind in nums) and (ind not in filterset)]
    index = [i for i in range(len(nums)) if nums[i] in value ]

    return index 
print(twoSum2(a, 6))











