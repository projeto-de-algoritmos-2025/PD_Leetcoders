class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        transactions = 2
        n = len(prices)
        dp = [[0] * n for _ in range(transactions + 1)]

        for i in range(1, transactions + 1):
            max_diff = -prices[0]
            
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[transactions][n - 1]
