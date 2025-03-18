# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        removed_list = []
        ans = []
        blocked = False
        for comment in source:
            comment.strip()
            i = 0
            while i < len(comment):
                if  not blocked:
                    if i == len(comment) - 1:
                        ans.append(comment[i])
                    else:
                        sub_comment = comment[i: i + 2]
                        if sub_comment == "/*":
                            blocked = True
                            i += 1
                        elif sub_comment == "//":
                            break 
                        else:
                            ans.append(comment[i])
                else:
                    sub_comment = comment[i: i + 2]
                    if sub_comment == "*/":
                        blocked = False
                        i += 1
                i += 1
            if ans and not blocked:
                removed_list.append("".join(ans))
                ans = []
                    


        return removed_list





        