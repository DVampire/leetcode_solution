from collections import Counter


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        # 保证元素个数小的数组在前
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (m + n + 1) // 2

        left = 0
        right = m

        # 二分查找m1的位置
        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1

            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1

        # 找nums1[m1-1]和nums2[m2-1]的最大值
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))

        # 中位数是c1
        if (m + n) % 2 == 1:
            return c1

        # 找nums1[m1]和nums2[m2]的最小值
        c2 = min(nums1[m1] if m1 < m else float("inf"), nums2[m2] if m2 < n else float("inf"))

        # 中位数是二者均值
        return (c1 + c2) / 2.0