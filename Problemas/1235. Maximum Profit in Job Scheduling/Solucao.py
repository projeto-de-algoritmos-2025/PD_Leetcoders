import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # ordenado por endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]  # endTime, maior profit

        for s, e, p in jobs:
            # Encontra o índice do último trabalho em q endTime <= s
            i = bisect.bisect_right(dp, (s, float('inf'))) - 1
            current_profit = dp[i][1] + p
            # Se o lucro atual é maior q o último lucro armazenado ele é adicionado em dp
            if current_profit > dp[-1][1]:
                dp.append((e, current_profit))

        return dp[-1][1]
