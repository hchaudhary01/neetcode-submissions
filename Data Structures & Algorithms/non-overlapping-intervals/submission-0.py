class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals = [[1,2],[2,4],[1,4]]
        intervals.sort(key = lambda x:x[1])
        prevEnd = intervals[0][1]
        res = 0 
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]
        return res


