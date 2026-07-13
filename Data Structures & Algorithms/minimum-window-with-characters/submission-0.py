class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        have = 0
        need_types = len(need)
        left = 0
        res = [-1, -1]
        res_len = float("inf")
        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            while have == need_types:
                current_len = right - left + 1
                if current_len < res_len:
                    res = [left, right]
                    res_len = current_len
                
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        if res_len == float("inf"):
            return ""

        return s[res[0]:res[1]+1]

                