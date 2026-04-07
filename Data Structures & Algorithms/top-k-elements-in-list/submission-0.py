class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        sorted_d = dict(sorted(
            d.items(), 
            key=lambda item: item[1],
            reverse=True))
        
        res = []
        for key, val in sorted_d.items():
            res.append(key)
            k -= 1
            if k == 0:
                break
        
        return res