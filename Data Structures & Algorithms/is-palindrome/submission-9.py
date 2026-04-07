class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(c):
            return (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')
        
        i, j = 0, len(s) - 1
        while i < j:
            h, t = s[i].upper(), s[j].upper()
            while not isAlphanumeric(h):
                i += 1
                if i >= len(s):
                    break
                h = s[i].upper()
            while not isAlphanumeric(t):
                j -= 1
                if j < 0:
                    break
                t = s[j].upper()
            if i <= j and h != t:
                return False
            i, j = i + 1, j - 1

        return True

