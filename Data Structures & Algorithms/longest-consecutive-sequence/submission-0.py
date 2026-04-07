class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        hashMaps = {}
        for num in nums:
            if num - 1 not in setOfNums:
                hashMaps[num] = 1
        res = 0
        for k, v in hashMaps.items():
            i = k + 1
            l = 1
            while i in setOfNums:
                l += 1
                i += 1
            res = max(res, l)
        return res
