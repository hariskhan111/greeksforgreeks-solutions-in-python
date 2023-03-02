"""
https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&sortBy=submissions
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).
"""
# python solution 

class Solution:

    def ispar(self,x):

        

        stack = []

        brackets =  ["(", "[", "{"]

        for i in x:

            if i in brackets:

                stack.append(i)

            else:

                if len(stack) == 0:

                    return False

                current_char= stack.pop()

                

                if  current_char == "(":

                    if i != ")":

                        return False

                        

                if  current_char == "[":

                    if  i!= "]":

                        return False

                        

                if  current_char == "{":

                    if i != "}":

                        return False
      

        if stack:

            return False

        return True


cls = Solution()
N = "{([])}"
result = cls.ispar(N)
print(result)
