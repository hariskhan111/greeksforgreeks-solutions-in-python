"""
https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?page=1&sortBy=submissions
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
"""
class Solution:
    def sort012(self,arr,n):
        return arr.sort()


cls = Solution()
N = 5
arr = [0,2,1,2,0]
result = cls.sort012(arr, N)
print(result)
