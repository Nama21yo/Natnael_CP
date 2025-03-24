# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def generate_string(n, i, output, count_zeros):
            if i == n:
                ans.append("".join(output[:]))
                return 
            if len(output) == 0 or (len(output) >= 1 and output[-1] != "0"):
                output.append("0")
                generate_string(n, i + 1, output, count_zeros + 1)
                output.pop()
            output.append("1")
            generate_string(n, i + 1, output, count_zeros)
            output.pop()

        generate_string(n, 0, [], 0)
        return ans