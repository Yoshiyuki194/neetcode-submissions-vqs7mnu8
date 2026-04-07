class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
        self.top_st, self.top_min_st = 0, 0

    def push(self, val: int) -> None: 
        if self.top_st == len(self.st):
            self.st.append(val)
        else:
            self.st[self.top_st] = val
        self.top_st += 1
        
        current_min = val
        if self.top_min_st > 0:
            current_min = min(val, self.min_st[self.top_min_st - 1])
            
        if self.top_min_st == len(self.min_st):
            self.min_st.append(current_min)
        else:
            self.min_st[self.top_min_st] = current_min
        self.top_min_st += 1

    def pop(self) -> None: 
        self.top_min_st -= 1
        self.top_st -= 1

    def top(self) -> int:
        return self.st[self.top_st - 1]

    def getMin(self) -> int:
        return self.min_st[self.top_min_st - 1]