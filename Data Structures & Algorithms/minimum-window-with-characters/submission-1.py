class Solution:
    def minWindow(self, s: str, t: str) -> str:
        reslen = float('inf')
        res = [-1,-1]

        tcount = defaultdict(int)
        for char in t:
            tcount[char] +=1
        
        scount = defaultdict(int)
        have = 0
        need = len(tcount)
        l = 0
        for i in range(len(s)):
            scount[s[i]]+=1
            if s[i] in tcount and scount[s[i]]==tcount[s[i]]:
                have +=1
            while have == need :
                if reslen > i-l+1:
                    reslen = i-l+1
                    res=[l,i]
                scount[s[l]]-=1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        if res[0]!=-1:
            return s[res[0]:res[1]+1]
        else:
            return ""


