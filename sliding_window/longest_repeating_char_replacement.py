class Solution(object):
    def character_replacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = {}
        max_length = 0
        left_index = 0
        right_index = 0

        for i in range(len(s)):
            char_count[s[right_index]] = char_count.get(s[right_index], 0) + 1
            window_length = right_index - left_index + 1
            max_freq = max(char_count.values())
            if window_length - max_freq > k:
                char_count[s[left_index]] -= 1
                left_index += 1
                window_length -= 1
            right_index += 1
            max_length = max(max_length, window_length)
        return max_length


# Test cases
sol = Solution()

s = "ABAB"
k = 2
assert sol.character_replacement(s, k) == 4

s = "AABABBA"
k = 1
assert sol.character_replacement(s, k) == 4
