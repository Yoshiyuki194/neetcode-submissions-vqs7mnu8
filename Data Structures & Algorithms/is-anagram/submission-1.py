class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab = {}
        for c in s:
            if c in vocab:
                vocab[c] += 1
            else:
                vocab[c] = 1
        for c in t:
            if c in vocab:
                vocab[c] -= 1
                if vocab[c] < 0:
                    return False
            else:
                return False
        for c in vocab:
            if vocab[c] > 0:
                return False
        return True