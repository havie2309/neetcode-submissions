class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]

        for current in intervals:
            if current[0] <= res[-1][1]:
                res[-1][1] = max(current[1], res[-1][1])
            else:
                res.append(current)
        return res

        
        
