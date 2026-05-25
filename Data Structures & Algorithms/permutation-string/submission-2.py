class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        count = {}
        window = {}

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        left = 0

        for right in range(len(s2)):
            window[s2[right]] = 1 + window.get(s2[right], 0)

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if window == count:
                return True

        return False
        


