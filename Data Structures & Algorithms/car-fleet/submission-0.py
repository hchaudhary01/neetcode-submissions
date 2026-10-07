class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nums=[]
        st = []
        for i in range(len(position)):
            nums.append((position[i],speed[i]))
        nums.sort(reverse=True)
        for p,s in nums:
            time = (target-p)/s
            if not st:
                st.append(time)
            else:
                if st[-1]<time:
                    st.append(time)
        return len(st)