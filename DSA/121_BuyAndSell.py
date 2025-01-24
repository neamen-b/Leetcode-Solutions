from typing import List
import math
class Solution:

    def maxProfit(prices: List[int]) -> int:
        lowest_price = float("inf")
        maximum_profit = 0

        for index in range(len(prices)):
            
            if(prices[index] < lowest_price):
                lowest_price = prices[index]
            if(prices[index] - lowest_price > maximum_profit):
                maximum_profit = prices[index] - lowest_price
        
        return maximum_profit
    


    # O(n^2) solution that might work
    # Works but is extremely inefficient. 
    # There is no point on working on a solution if you know it is not going to be efficient


    def BuyAndSell2(prices: List[int]) -> int:
        array_of_differences = []

        for i in range(len(prices)):

            for j in range(i+1,len(prices)):

                if( (prices[j]-prices[i]) > 0):
                    array_of_differences.append(prices[j]-prices[i])
        
        if(array_of_differences):
            return max(array_of_differences)
        else:
            return 0


#print(Solution.BuyAndSell(test_prices))
