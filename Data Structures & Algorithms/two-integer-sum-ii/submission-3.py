class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = defaultdict()
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in dict:
                return [dict[diff], i + 1]
            dict[numbers[i]] = i + 1

        