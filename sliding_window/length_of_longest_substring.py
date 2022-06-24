class Solution(object):
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        chars = set()
        left_index = 0

        for right_index, char in enumerate(s):
            while char in chars:
                chars.remove(s[left_index])
                left_index += 1
            chars.add(char)
            max_length = max(max_length, right_index - left_index + 1)
        return max_length


# Test cases
sol = Solution()
assert sol.length_of_longest_substring("abcabcbb") == 3
assert sol.length_of_longest_substring("bbbbb") == 1
assert sol.length_of_longest_substring("pwwkew") == 3
