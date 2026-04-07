class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        codes = {}
        for st in strs:
            code = ''
            for i in range(ord('a'), ord('z') + 1):
                fr = 0
                for c in st:
                    if i == ord(c):
                        fr += 1
                code += chr(i) + str(fr)
            if code in codes:
                codes[code].append(st)
            else:
                codes[code] = [st]
        res = []
        for _, v in codes.items():
            res.append(v)
        return res
