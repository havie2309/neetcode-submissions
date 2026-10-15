class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 # swap 2 array if size 1 > size 2

        left, right = 0, len(nums1) - 1
        while True:
            i = (left+right)//2
            j = half - i - 2

            left1 = nums1[i] if i >= 0 else -9999999
            right1 = nums1[i+1] if i+1 < len(nums1) else 9999999
            left2 = nums2[j] if j >= 0 else -9999999
            right2 = nums2[j+1] if j+1 < len(nums2) else 9999999

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (min(right1, right2) + max(left1, left2)) / 2
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1


        