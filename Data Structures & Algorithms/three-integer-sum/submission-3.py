class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res_dup = []

        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                t = nums[j] + nums[k]
                if t == -nums[i]:
                    res_dup.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                elif t > -nums[i]:
                    k -= 1
                else:
                    j += 1

        if not res_dup:
            return res_dup

        res = [res_dup[0]]
        for i in range(1, len(res_dup)):
            dup = False
            for j in range(0, i):
                if res_dup[i] == res_dup[j]:
                    dup = True
                    break
            if not dup:
                res.append(res_dup[i])

        return res
            

