class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
                #print(res, "no overlap happened")
            elif res[-1][1] <= intervals[i][1]:
                res[-1][1] = intervals[i][1]
                #print(res, "overlap happened")
        return res