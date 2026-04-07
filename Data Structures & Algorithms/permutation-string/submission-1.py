class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - 97] += 1
        l = 0
        for r in range(len(s2)):
            if r - l == len(s1):
                freq[ord(s2[l]) - 97] += 1
                l += 1
            freq[ord(s2[r]) - 97] -= 1
            s = 0
            for i in range(26):
                s += max(0, freq[i])
            if s == 0:
                return True
        return False