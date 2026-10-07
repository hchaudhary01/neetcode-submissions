class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = [0]*n
        for i in range(n):
            pos_speed[i] = (position[i], speed[i])
        pos_speed.sort(reverse = True)
        #print(pos_speed)

        st = []
        for i in range(n):
            time = (target-pos_speed[i][0])/pos_speed[i][1]
            if st and st[-1] < time:
                st.append(time)
            if not st:
                st.append(time)
        #print(st)
        return len(st)