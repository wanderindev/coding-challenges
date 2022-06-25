class Solution(object):
    def get_char_index(self, char):
        return ord(char) - ord("a")

    def populate_list(self, s, c):
        l = [0] * 26
        for i in range(c):
            index = self.get_char_index(s[i])
            l[index] += 1
        return l

    def get_initial_matches(self, l1, l2):
        matches = 0
        for i in range(26):
            matches += 1 if l1[i] == l2[i] else 0
        return matches

    def check_inclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        left_index = 0
        s1_chars = self.populate_list(s1, len(s1))
        s2_chars = self.populate_list(s2, len(s1))
        matches = self.get_initial_matches(s1_chars, s2_chars)

        for right_index in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = self.get_char_index(s2[right_index])
            s2_chars[index] += 1
            if s1_chars[index] == s2_chars[index]:
                matches += 1
            elif s1_chars[index] + 1 == s2_chars[index]:
                matches -= 1

            index = self.get_char_index(s2[left_index])
            s2_chars[index] -= 1
            if s1_chars[index] == s2_chars[index]:
                matches += 1
            elif s1_chars[index] - 1 == s2_chars[index]:
                matches -= 1
            left_index += 1
        return matches == 26

# Test cases
sol = Solution()

s1 = "ab"
s2 = "eidbaooo"
assert sol.check_inclusion(s1, s2)

s1 = "ab"
s2 = "eidboaoo"
assert not sol.check_inclusion(s1, s2)
