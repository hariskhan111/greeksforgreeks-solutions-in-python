"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray (irrespective of its size). 
You shouldn't return any array, modify the given array in-place.
Example 1:
Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
"""

class Solution:	
    def reverseInGroups(self, arr, N, K):

        for i in range(0,len(arr),K):

            start=i 
            end=min(i+K-1,len(arr)-1),
            end = end[0]         

            while(start<end):

                arr[start],arr[end]=arr[end],arr[start]

                start+=1

                end-=1

        return arr 

cls = Solution()
N, K = 9, 4
arr = [1,2,3,4,5,6,7,8,9]
result = cls.reverseInGroups(arr, N, K)
print(result)