class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            l, h = i + 1, n - 1
            while l <= h:
                m = (l + h) // 2
                if numbers[m] == target - numbers[i]:
                    return [i + 1, m + 1]
                elif numbers[m] < target - numbers[i]:
                    l = m + 1
                else:
                    h = m - 1