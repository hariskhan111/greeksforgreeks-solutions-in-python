"""
https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&sortBy=submissions
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).
"""
# python solution 
import re
class Solution:

    def isHTML(self,x):

        tags = re.findall(r'<[^>]+>', x)

        stack = []
     
        brackets =  ["<div>", "<b>", "<p>", "<i>", "<em>"]

        for i in tags:

            if i in brackets:

                stack.append(i)

            else:

                if len(stack) == 0:

                    return False

                current_char= stack.pop()

                

                if  current_char == "<div>":

                    if i != "</div>":

                        return "div"

                        

                if  current_char == "<b>":

                    if  i!= "</b>":

                        return "b"

                        

                if  current_char == "<p>":

                    if i != "</p>":

                        return "p"
                
                if  current_char == "<em>":

                    if i != "</em>":

                        return "em"
      

        if stack:

            return str(stack[0].replace("<","").replace(">",""))

        return "True"


cls = Solution()
N = "<div>yes</div><i><b><p>hello world</p></b>"
result = cls.isHTML(N)
print(result)
