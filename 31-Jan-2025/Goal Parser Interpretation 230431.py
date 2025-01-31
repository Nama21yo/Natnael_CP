# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        goal_parser = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                goal_parser.append("G")
                i += 1
            elif (i + 1) != len(command) and command[i] == "(" and command[i + 1] == ")":
                goal_parser.append("o")
                i += 2
            else:
                goal_parser.append("al")
                i += 4
        return "".join(goal_parser)

        