class Solution:
    def two_sum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            total = numbers[left_pointer] + numbers[right_pointer]
            if total > target:
                right_pointer -= 1
            elif total < target:
                left_pointer += 1
            else:
                return [left_pointer + 1, right_pointer + 1]


# Test cases
sol = Solution()

numbers = [2, 7, 11, 15]
target = 9
assert sol.two_sum(numbers, target) == [1, 2]

numbers = [2, 3, 4]
target = 6
assert sol.two_sum(numbers, target) == [1, 3]

numbers = [-1, 0]
target = -1
assert sol.two_sum(numbers, target) == [1, 2]
