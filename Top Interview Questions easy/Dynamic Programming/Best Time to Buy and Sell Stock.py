class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        m_pr = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = prices[i]
            elif prices[i] > max_price:
                max_price = prices[i]
                
            tmp = max_price - min_price
            if tmp > m_pr:
                m_pr = tmp
        return m_pr


sol = Solution()
arr = [7,1,5,3,6,4]
print(sol.maxProfit(arr))
