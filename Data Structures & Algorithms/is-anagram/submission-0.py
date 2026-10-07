class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d={}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        
        for char in t:
            if char not in d:
                return False
            if d[char] <=0:
                return False
            else:
                d[char]-=1
        return True
