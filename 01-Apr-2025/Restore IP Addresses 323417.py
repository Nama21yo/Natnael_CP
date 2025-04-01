# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        if len(s) < 4 or len(s) > 12:
            return res
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return
            for length in range(1, 4):
                if start + length <= len(s):
                    part = s[start:start + length]
                    if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                        continue
                    backtrack(start + length, parts + [part])
        backtrack(0, [])
        
        return res
