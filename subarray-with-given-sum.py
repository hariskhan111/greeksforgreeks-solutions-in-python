"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&sortBy=submissions

Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.
"""
class Solution:
    def subArraySum(self,arr, n, s): 
        A = []
        curr_sum = arr[0]
        start = 0
        i = 1
        while i <= n:
            while curr_sum > s and start < i-1:
                curr_sum = curr_sum - arr[start]
                start += 1
            if curr_sum == s:
                A.append(start+1)
                A.append(i)
                return A

            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1

        A.append(-1)
        return A

cls = Solution()
N, S = 5, 12
arr = [1,2,3,7,5]
result = cls.subArraySum(arr, N, S)
print(result)