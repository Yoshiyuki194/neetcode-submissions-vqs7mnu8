class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [-1] * n, [n] * n

        st = []
        for i in range(0, n):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                l[i] = st[-1]
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                r[i] = st[-1]
            st.append(i)

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (r[i] - l[i] - 1))

        return res