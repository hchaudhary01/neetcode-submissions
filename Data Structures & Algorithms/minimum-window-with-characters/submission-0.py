class Solution:
    def minWindow(self, s: str, t: str) -> str:
        reslen = float('inf')
        res = [-1,-1]

        tcount = {}
        scount = defaultdict(int)
        for char in t:
            if char not in tcount:
                tcount[char]=1
            else:
                tcount[char]+=1

        have = 0
        required = len(tcount)

        l=0
        for r in range(len(s)):
            scount[s[r]]+=1
            #print(scount, "scount in for")
            if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                have+=1
            while have == required:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res=[l,r]    
                scount[s[l]]-=1
                #print(scount, "scount in while")
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        l = res[0]
        r = res[1]
        if res[0]!=-1:
            return s[l:r+1]
        else:
            return ""


