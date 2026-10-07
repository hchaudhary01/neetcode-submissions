class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            #print(a,b)
            if b > a:
                heapq.heappush(stones, a-b)
        return abs(stones[0]) if len(stones)>0 else 0

        