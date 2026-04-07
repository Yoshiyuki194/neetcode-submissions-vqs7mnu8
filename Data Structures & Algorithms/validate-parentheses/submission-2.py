class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '}': '{',
            ')': '(',
            ']': '[',
            '{': '',
            '(': '',
            '[': ''
        }
        st, top = [''] * len(s), 0
        for c in s:
            if top > 0 and st[top - 1] == bracket_map[c]:
                    top -= 1
            else:
                st[top] = c
                top += 1
        print(top)
        return not top