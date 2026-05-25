class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = 0 
        longest = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            freq = max(freq, count[s[right]])

            while (right - left + 1) - freq > k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest


        