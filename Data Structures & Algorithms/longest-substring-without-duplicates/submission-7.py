class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for c in range(len(s)):
            while s[c] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[c])
            res = max(res,len(seen))
        return res