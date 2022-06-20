from collections import defaultdict


class Solution:
    def group_anagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        char_to_index = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25,
        }

        for word in strs:
            count = [0] * 26
            for char in word:
                count[char_to_index[char]] += 1
            result[tuple(count)].append(word)
        return result.values()


# Test cases
sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = sol.group_anagrams(strs)
expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
actual = sorted([[word for word in sorted(group)] for group in res])
assert len(expected) == len(actual) and expected == actual

strs = [""]
res = sol.group_anagrams(strs)
expected = sorted([[""]])
actual = [[word for word in sorted(group)] for group in res]
assert len(expected) == len(actual) and expected == actual

strs = ["a"]
res = sol.group_anagrams(strs)
expected = sorted([["a"]])
actual = [[word for word in sorted(group)] for group in res]
assert len(expected) == len(actual) and expected == actual
