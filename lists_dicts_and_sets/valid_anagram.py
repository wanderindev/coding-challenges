class Solution(object):
    def is_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t):
            return False

        chars_s = {}
        chars_t = {}

        for i in range(len(s)):
            chars_s[s[i]] = chars_s[s[i]] + 1 if s[i] in chars_s else 1
            chars_t[t[i]] = chars_t[t[i]] + 1 if t[i] in chars_t else 1

        for key, val in chars_s.items():
            if key not in chars_t or not chars_s[key] == chars_t[key]:
                return False

        return True


# Test cases
sol = Solution()

assert sol.is_anagram("anagram", "nagaram")
assert not sol.is_anagram("rat", "cat")
assert not sol.is_anagram("aacc", "ccac")
