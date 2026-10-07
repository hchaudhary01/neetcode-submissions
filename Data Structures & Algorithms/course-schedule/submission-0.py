class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for u,v in p:
            adj[u].append(v)
        
        path = set()
        visited = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for i in adj[node]:
                if not dfs(i):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True  
        for i in range(n):
            if not dfs(i):
                return False
        return True
        