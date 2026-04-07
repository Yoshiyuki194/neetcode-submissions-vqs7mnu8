class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [-1] * len(height), [-1] * len(height)
        left[0], right[len(height) - 1] = -1, -1
        for i in range(1, len(height)):
            if left[i - 1] == -1:
                if height[i] > height[i - 1]:
                    left[i] = -1
                else:
                    left[i] = height[i - 1]
            else:
                if height[i] > left[i - 1]:
                    left[i] = -1
                else:
                    left[i] = left[i - 1]
        for i in range(len(height) - 2, -1, -1):
            if right[i + 1] == -1:
                if height[i] > height[i + 1]:
                    right[i] = -1
                else:
                    right[i] = height[i + 1]
            else:
                if height[i] > right[i + 1]:
                    right[i] = -1
                else:
                    right[i] = right[i + 1]
        res = 0
        for i in range(1, len(height) - 1):
            if left[i] > -1 and right[i] > -1:
                res += min(left[i], right[i]) - height[i]
        return res
            
            