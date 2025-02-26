# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        # . >> current directory
        # .. >> parent directory
        # // or //// = /
        #  ... or ...... >> fileNames
        directory = path.split("/")
        stack = []

        for dir in directory:
            # if ir is '', .,
            if dir == "" or dir == ".":
                continue
            elif dir == "..":
                # if my stack isn't empty pop it
                if stack: 
                    stack.pop()
            else:
                stack.append(dir)  

        return "/" + "/".join(stack)
        