class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = [key for key, _ in count.most_common(k)]
        return result


            
            
        