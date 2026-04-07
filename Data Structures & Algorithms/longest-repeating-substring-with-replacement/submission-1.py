class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        ans = 0
        maxFreq = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            maxFreq = max(maxFreq, freq[s[i]])
            if i - l + 1 - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
                maxFreq = max(freq.values())
            ans = max(ans, i - l + 1)
        return ans