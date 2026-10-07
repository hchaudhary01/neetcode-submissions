class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        i = 0
        j = k-1

        while j<len(nums):
            max_el = max(nums[i:j+1])
            #print("window is ", nums[i:j+1])
            ans.append(max_el)
            #print(max_el," max_el and ans " ,ans)
            i+=1
            j+=1
        return ans