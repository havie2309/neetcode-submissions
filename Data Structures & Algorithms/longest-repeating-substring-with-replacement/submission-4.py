class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        freq = {}
        res = 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            longest = max(longest, freq[s[right]])
            if right - left + 1 - longest > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
                


        