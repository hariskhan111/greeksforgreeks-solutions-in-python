class Solution:

    def duplicates(self, arr, n): 

        p=[0]*10000
        
        s=[]

        for i in arr:

            p[i]+=1

        for i in range(len(p)):

            if p[i]>1:

                s.append(i)

        s.sort()

        if len(s)>=1:

            return s

        else:

            s.append(-1)

            return s 


clx = Solution()
n, arr = 26, [13, 9, 25, 1, 1, 0, 22, 13, 22, 20, 3, 8, 11, 25, 10, 3, 15, 11, 19, 20, 35, 4, 25, 14, 23, 14]
res = clx.duplicates(arr, n)
print(res)