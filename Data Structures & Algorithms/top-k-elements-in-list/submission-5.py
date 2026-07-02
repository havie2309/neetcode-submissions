from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for num in range(len(freq)-1, 0, -1):
            for i in freq[num]:
                res.append(i)
                if len(res) == k:
                    return res


            
            
        