from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = Counter(nums)
        result = []
        sorted_dict = dict(sorted(lst.items(), key=lambda item: item[1]))
        for key in reversed(sorted_dict):
            if k > 0:
                result.append(key)
            k -= 1
        return result        

            
            
        