class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n
        for i in range(0, n):
            pre[i] = pre[max(0, i - 1)] * nums[i]
        for i in range(n - 1, 0, -1):
            suf[i] = suf[min(n - 1, i + 1)] * nums[i]
        res = [suf[1]]
        for i in range(1, n - 1):
            res.append(pre[i - 1] * suf[i + 1])
        res.append(pre[n - 2])
        return res