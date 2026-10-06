from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       keys = count.most_common()
       keys.reverse() 

       result = []
       while k > 0:
        item_tuple = keys.pop()
        result.append(item_tuple[0])
        k -= 1
       return result 
       