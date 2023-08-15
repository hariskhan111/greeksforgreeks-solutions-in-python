"""
https://practice.geeksforgeeks.org/problems/second-largest3735/1?page=1&sortBy=submissions
"""

class Solution:

	def print2largest(self,arr, n):
	    if not arr:
	        return -1
	    
        dup = set(arr)
	    
        dup_list = list(dup)
	    
        if len(dup_list) < 2:
	        return -1
	        
		dup_list.sort()
		dup_list.reverse()
	
		return dup_list[1]


cls = Solution()
cls.print2largest([21,45,23,13,65,34],6)