'''
Best time to buy and sell stocks

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1=5.
            Not 7-1 = 6, as selling price needs to be larger than buying price

Buy low and sell high
we are given an input array, each value represents price of the stock at particular day. Buy on 1 of these day and sell another day.
we want to maximeize our profit. 
We cant sell 7 first and because time moves in one direction right. Also, didn't buy that to sell. We cant go back in time sell at that price.

We are using two pointer technique to solve this problem.
We are gonna initialize a left pointer on day 1 and right on day 2 and we check what is the current profit.
In the first case it is going from 7 to 1 which is -ve. left = buy, right = sell
why would we buy left when we can buy right i.e 1. right is less than left. 
thats how the algorithm works. since, right value is less than left, we are going to update our pointer left.
So, left is gonna be on day 2 and right on day 3, now we see right value is greater than left value, whats the profit
5-1=4 which is max profit for now. Since, in this case our left pointer is less than our right pointer. since we are buying
low and selling high. That means we can leave our left pointer and only update our right pointer. Now, lets compare our
L and R. we aer buying here and sell 3-2 = 1 which is less than our current profit. We are not going to update our max profit
Again, we notice that left pointer is less than right pointer we still update our right pointer. Now, we get to our result
case and  6 and 1 which has max profit of 5. Now, we update our max profit from 4 to 5. Now, our algorithm is gonna go until it check's 
for every posible value even though we can see that 5 is the max profit. The last case here is buying in 1 and selling at 4
which has profit of 3 and still have max profit 5.
Our algorithm is complete.
If we wanna know the memory and extra stuff we used, we know we really didn't use any extra memory.
We only used pointers but no arrays so, extra memory is O(1)
Time is gonna be linear since it is a two pointer solution and we are not doing any brute force stuff.
O(n). We only have to scan throught the array 1 time, even though we had two pointers.
'''
class BestTimeTBASS:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy and right = sell pointers initialize to 0 and 1 respectively
        maxP = 0 # initializing max profit to 0

        while r < len(prices): # iterate until the right pointer hasn't passed through end of the array
            # profitable ?
            if prices[l] < prices[r]: # if buying is less than selling
                profit = prices[r] - price[l]
                maxP = max(maxP, profit) # we can potentially update our max profit by checking the maximum value of the current profit and just conmpute profit
            else: # if not profitable transaction
                l += r # shift the left pointer to the right because we foind a really low price that we could; left pointer will be minimum here
            r += 1 #regardless of the conditions we have to update our right pointer
        return maxP # keep going until right poiinter is out of bounds and max is