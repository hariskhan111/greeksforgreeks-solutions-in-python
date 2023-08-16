"""
https://practice.geeksforgeeks.org/problems/peak-element/1?page=2&sortBy=submissions
"""

def peakElement(arr, n):
    for i in range(n):
        if i == 0 and len(arr) == 1:
            return 1
        if i == 0 and arr[i] >= arr[i+1]:
            return 1
        elif i == n-1:
            if arr[i] >= arr[i-1]:
                return 1
            else:
                return 0
        elif arr[i] >= arr[i+1] and arr[i] >= arr[i-1]:
            return 1

print(peakElement([6, 1, 15, 19, 9, 13, 12, 6, 7, 2, 10, 4, 1, 14, 11, 14, 14, 13],18))