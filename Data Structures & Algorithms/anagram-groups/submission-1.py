class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for st in strs:
            key = [0]*26
            for j in st:
                key[ord(j)-ord('a')]+=1
            key = tuple(key)
            if key not in d:
                d[key]=[]
            d[key].append(st)
        return list(d.values())
