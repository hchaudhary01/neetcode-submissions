class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_val = val
        if self.st and self.st[-1][1] < val:
            min_val = self.st[-1][1]
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        
