class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        for i in range(len(arr)-1):
            if(i%2==0 and arr[i]>arr[i+1]):
                l=arr[i+1] #4
                arr[i+1]=arr[i]
                arr[i]=l
            elif(i%2!=0 and arr[i]<arr[i+1]):
                l=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=l
                
        return arr