class Solution:
    def longest_consecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_sequence = 0
        set_of_nums = set(nums)

        for num in nums:
            if num - 1 not in set_of_nums:
                sequence_length = 1
                while num + sequence_length in set_of_nums:
                    sequence_length += 1
                longest_sequence = max(longest_sequence, sequence_length)
        return longest_sequence


# Test cases
sol = Solution()

nums = [100, 4, 200, 1, 3, 2]
assert sol.longest_consecutive(nums) == 4

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
assert sol.longest_consecutive(nums) == 9
