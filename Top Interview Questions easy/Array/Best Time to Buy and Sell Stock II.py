class Solution:
     def maxProfit(self, prices: list[int]) -> int:
        def findBuy(prices: list[int], searchStart: int) -> (int, int):
            res = prices[searchStart]
            resIndex = searchStart
            index = searchStart + 1
            while index < len(prices) and prices[index] <= res:
                res = prices[index]
                resIndex = index  
                index += 1
            return res, resIndex


        def findSell(prices: list[int], searchStart: int) -> (int, int):
            res = prices[searchStart]
            resIndex = searchStart
            index = searchStart + 1
            while index < len(prices) and prices[index] >= res:
                res = prices[index]
                resIndex = index  
                index += 1
            return res, resIndex
        

        searchForBuyFromIndex = 0
        buy = prices[searchForBuyFromIndex]
        searchForSellFromIndex = 0
        sell = prices[searchForSellFromIndex]
        profit = 0
        while True:
            buy, searchForSellFromIndex = findBuy(prices, searchForBuyFromIndex)
            sell, searchForBuyFromIndex = findSell(prices, searchForSellFromIndex)
            profit += sell - buy
            if buy == sell:
                break
        return profit


prices = [1,2,3,4,5]
sol = Solution()
print(sol.maxProfit(prices))

            
