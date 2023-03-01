"""
https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
"""
class Solution:
    def MissingNumber(self,array,n):
        self.l = array
        self.l.sort()
        val , res = 1 , 0
        for i in self.l:
            if i != val:
                res = val
                break
            val += 1
        if res == 0: return i+1
        else: return res

cls = Solution()
N = 5
arr = [1,2,3,5]
result = cls.MissingNumber(arr, N)
print(result)