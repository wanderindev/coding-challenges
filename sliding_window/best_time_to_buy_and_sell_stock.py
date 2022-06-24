class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = 1
        max_profit = 0

        if len(prices) == 1:
            return max_profit

        for i in range(len(prices)):
            if prices[left_index] < prices[right_index]:
                max_profit = max(
                    max_profit, prices[right_index] - prices[left_index]
                )
            else:
                left_index = right_index
            if right_index < len(prices) - 1:
                right_index += 1
        return max_profit


# Test cases
sol = Solution()

prices = [7, 1, 5, 3, 6, 4]
assert sol.max_profit(prices) == 5

prices = [7, 6, 4, 3, 1]
assert sol.max_profit(prices) == 0

prices = [1]
assert sol.max_profit(prices) == 0

prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
assert sol.max_profit(prices) == 9
