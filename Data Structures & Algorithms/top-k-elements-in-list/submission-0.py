class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        bucket = [[] for i in range(len(nums)+1)]
        #print(bucket)
        for num in nums:
            if num not in counter:
                counter[num]=1
            else:
                counter[num]+=1
        #print(counter, "counter")
        for val, count in counter.items():
            bucket[count].append(val)
        #print(bucket, "bucket")

        ans =[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                #print(num, "num and bucket[i] ", bucket[i])
                ans.append(num)
                if len(ans) == k:
                    return ans

        