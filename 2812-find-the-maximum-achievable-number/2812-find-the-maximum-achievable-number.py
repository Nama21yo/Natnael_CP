class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # The num and maximum achievable numbers will always meet in the middle
        # The graph will be linear 
        return num + 2*(t)
        