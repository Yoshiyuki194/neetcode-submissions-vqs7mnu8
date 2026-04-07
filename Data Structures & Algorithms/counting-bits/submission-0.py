class Solution:
    def countBits(self, n: int) -> List[int]:
        def countEach(i):
            cnt = 0
            while i > 0:
                cnt += i & 1
                i >>= 1
            return cnt
        return [countEach(i) for i in range(0, n + 1)]
