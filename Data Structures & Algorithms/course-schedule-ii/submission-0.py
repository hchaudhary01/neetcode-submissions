class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for u,v in p:
            adj[u].append(v)
        
        path = set()
        visited = set()
        ans = []
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            path.remove(node)
            visited.add(node)
            ans.append(node)

            return True
        for i in range(n):
            if not dfs(i):
                return []
        return ans
        
