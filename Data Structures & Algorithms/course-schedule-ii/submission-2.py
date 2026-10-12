class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        ans = []

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == None:
                return True

            if preMap[crs] == []:
                ans.append(crs)
                preMap[crs] = None
                return True
            
            visited.add(crs)

            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            
            visited.remove(crs)
            preMap[crs]=None
            ans.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ans
