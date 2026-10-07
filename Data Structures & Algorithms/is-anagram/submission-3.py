class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        if len(s)!= len(t):
            return False
        for c in s:
            if c not in h:
                h[c]=1
            else:
                h[c]+=1
        
        for c in t:
            if c not in h or h[c]<=0:
                return False
            else:
                h[c]-=1
        return True