class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        i = 0
        j = len(people)-1
        ans = 0
        people.sort()
        while i<=j:
            if people[i]>=limit:
                ans+=1
                i+=1
            elif people[j]>=limit:
                ans+=1
                j-=1
            elif people[i]+people[j] <= limit:
                ans+=1
                i+=1
                j-=1
            elif people[i] + people[j]>limit:
                ans+=1
                j-=1

        return ans

