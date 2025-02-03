# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        masked = []
        if "@" in s:
            masked.append(s[0].lower())
            masked.append("*****")
            k = 0
            for i,char in enumerate(s):
                if char == "@":
                    masked.append(s[i - 1].lower())
                    masked.append("@")
                    k = i + 1
                elif char == ".":
                    masked.append(s[k:i + 1].lower())
                    masked.append(s[i+1:].lower())
        else:
            count = 0
            my_digit = []
            for char in s:
                if char.isdigit():
                    my_digit.append(char)
                    count += 1
            my_digit = "".join(my_digit)
            print("count",count)
            if count == 10:
                masked.append("***-***-")
                masked.append(my_digit[6:])
            else:
                rem = count - 10
                masked.append("+")
                masked.append("*"*rem)
                masked.append("-***-***-")
                masked.append(my_digit[6 + rem:])
        return "".join(masked)


        