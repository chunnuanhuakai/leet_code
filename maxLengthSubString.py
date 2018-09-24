# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:14:04 2018

@author: liuHongBing
"""

## 给定一个字符串，找出不含有重复字符的最长子串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if  s=='':
            return 0
        
        for i in range(len(s), -1, -1):
            for index in range(0, len(s)-i+1 ):
                tmp = s[index:index+i]
                if len(tmp) == len(set(tmp)):
                    return i
                
     
    def getTrue(self,mid, s):
        
        for index in range(0, len(s)-mid+1):
            tmp = s[index: index+mid]
            if len(tmp)==len(set(tmp)):
                return True
        return False
                
            
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        min = 0
        max = len(s)
        
        maxlength = 0
        
        if self.getTrue(len(s), s):
            return len(s)
        
        while True:
            if max>1000:
                mid = (min + max) //10 
            else:
                mid = (min + max) //2
            
            if self.getTrue(mid, s) == False:
                min = min
                max = mid
            else:
                if mid >= maxlength:
                    maxlength = mid
                    min = mid
                    max = max
                else:
                    break
                
            if (max - min) <=1  :
                break
        return maxlength
    
    
