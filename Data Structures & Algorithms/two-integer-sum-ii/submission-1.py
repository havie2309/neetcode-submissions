class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in dic:
                return [dic[diff] + 1, i + 1]
            dic[num] = i
        return -1

        