class Solution:

    def encode(self, strs: List[str]) -> str:
        res, idx = '', str(len(strs)) + '|'
        for s in strs:
            res += s
            idx += str(len(s)) + '|'
        return idx + res

    def decode(self, s: str) -> List[str]:
        res = []
        splits = s.split('|')
        l = int(splits[0])
        idx = splits[1:l+1]
        offset = len(splits[0]) + 1 + sum(len(i) + 1 for i in idx)
        for i in idx:
            res.append(s[offset:offset+int(i)])
            offset += int(i)
        return res
