
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()
        s = e = 0
        count = 0
        ans = 0

        while s < len(intervals):
            if start[s]<end[e]:
                s +=1
                count+=1
            else:
                e+=1
                count -=1
            ans = max(ans,count)
        return ans




#0,5,15.   10,20,40
        