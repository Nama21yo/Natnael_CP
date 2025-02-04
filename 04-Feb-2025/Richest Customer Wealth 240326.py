# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich_wealth = 0
        n = len(accounts)
        for i in range(n):
            current_customer = 0
            for j in range(len(accounts[i])):
                current_customer += accounts[i][j]
            rich_wealth = max(current_customer, rich_wealth)
        return rich_wealth
            
        