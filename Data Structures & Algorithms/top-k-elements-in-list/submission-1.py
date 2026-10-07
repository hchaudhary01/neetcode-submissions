class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort where index is mentioning the frequency of element
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] += 1
        #print(count, "hashmap")
        for num, cnt in count.items():
            freq[cnt].append(num)
        #print(freq, "freq array")
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


