from collections import Counter


class Solution:
    def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count = {}
        list_of_counts = [[] for i in range(len(nums) + 1)]
        results = []

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        for count, num in num_count.items():
            list_of_counts[num].append(count)

        for i in range(len(list_of_counts) - 1, 0, -1):
            for num in list_of_counts[i]:
                results.append(num)
                if len(results) == k:
                    return results


# Test cases
sol = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2
assert sorted(sol.top_k_frequent(nums, k)) == [1, 2]

nums = [1]
k = 1
assert sol.top_k_frequent(nums, k) == [1]
