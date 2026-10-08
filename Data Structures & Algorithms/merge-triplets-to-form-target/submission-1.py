class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tripi = []
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                tripi.append(t)
        #print(tripi)
        if len(tripi) == 0:
            return False
        res = tripi[0]
        for i in range(1,len(tripi)):
            res=[max(res[0],tripi[i][0]), max(res[1],tripi[i][1]), max(res[2],tripi[i][2])]
        #print(res, "res")
        return res[0] == target[0] and res[1] == target[1] and res[2] == target[2]