"""
https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1?page=2&sortBy=submissions
"""

#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    first = head
    second = head
    
    for _ in range(n):
        if first is None:
            return -1
        
        first = first.next
        
    while first is not None:
        first = first.next
        second = second.next
        
    if second:
        return second.data
        
    return -1
    