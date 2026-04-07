from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hs = defaultdict(int)
        r = 0
        l, h = 0, 0
        hs[s[0]] += 1
        r = 1
        for i in range(1, len(s)):
            h += 1
            hs[s[i]] += 1
            while hs[s[i]] > 1:
                hs[s[l]] -= 1
                l += 1
            r = max(r, h - l + 1)
        return r