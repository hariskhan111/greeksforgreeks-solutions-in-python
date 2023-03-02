"""
https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?page=1&sortBy=submissions
Given an array A of positive integers. Your task is to find the leaders in the array. 
An element of array is leader if it is greater than or equal to all the elements to its right side. 
The rightmost element is always a leader. 
"""

#using monotonic stack
class Solution:

    def leaders(self, A, N):
        st = [1,4,6,78,3]

        for i in A:
            while st and i > st[-1]:
                print(st, i, st[-1])
                st.pop()

            st.append(i)

        return st


# class Solution:
#     def leaders(self, arr, N):
#         lst = []
#         j = 1
#         for i in range(N):
#             el = arr[i]
#             j = i + 1
#             is_leader = True
#             while j < N:
        
#                 if el < arr[j]:
#                     j+=1
#                     is_leader = False
#                     continue
                
#                 j += 1

#             if is_leader:
#                 lst.append(el)
            
#         return lst


cls = Solution()
N = 5
arr = [16,17,4,3,5,2]
result = cls.leaders(arr, N)
print(result)