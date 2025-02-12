# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill = skill[0] + skill[-1]
        l = 1
        r = len(skill) - 2
        entire_skill = 0
        while l < r:
            if skill[l] + skill[r] != total_skill:
                return -1
            entire_skill += (skill[l] * skill[r])
            l += 1
            r -= 1
        entire_skill += (skill[0]*skill[-1])
        return entire_skill