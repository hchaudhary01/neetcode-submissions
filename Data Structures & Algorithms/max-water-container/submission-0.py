class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        ma = 0
        while i<j:
            cur_height = min(heights[i],heights[j])*(j-i)
            ma = max(ma, cur_height)
            if heights[i] >= heights[j]:
                j-=1
            else:
                i+=1
        return ma