class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        t = [(target - x[0]) / x[1] for x in pairs]

        st = []
        for i in range(len(t)):
            if not st or st[-1] < t[i]:
                st.append(t[i])
        
        return len(st)
