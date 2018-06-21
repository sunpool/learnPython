class Solution:
    def findMedianSortedArray(self, nums1, nums2):
        """
        :param num1:
        :param num2:
        :return:
        """
        if len(nums1) <= len(nums2):
            m = len(nums1)
            m_nums = nums1
            n, n_nums = len(nums2), nums2
        else:
            # return self.findMedianSortedArray(nums2, nums1)
            n, n_nums = len(nums1), nums1
            m, m_nums = len(nums2), nums2

        # search in smaller loop
        i_start, i_end = 0, len(m_nums)
        half_len = (m+n+1)//2

        while i_start < i_end:
            i = (i_start + i_end) // 2
            j = half_len - i
            if i < m and n_nums[j-1] > m_nums[i]:
                i_start = i + 1
            elif i > 0 and n_nums[j] < m_nums[i-1]:
                i_end = i - 1
            else:
                if i == 0:
                    max_left = n_nums[j-1]
                elif j == 0:
                    max_left = m_nums[i-1]
                else:
                    max_left = max(n_nums[j-1], m_nums[i-1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = n_nums[j]
                elif j == n:
                    min_right = m_nums[i]
                else:
                    min_right = min(n_nums[j], m_nums[i])

                return (max_left + min_right) / 2






solution = Solution()
a = [1, 2, 3, 4, 5, ]
b = [2.1, 3.1, 4.1]
ret = solution.findMedianSortedArray(a, b)
print(ret)

a.extend(b)
a.sort()
print a
print a[len(a) / 2], len(a) / 2, len(a)
print

a = [1, 2, 3, 4, 5, 6]
b = [2.1, 3.1, 4.1]
ret = solution.findMedianSortedArray(a, b)
print(ret)

a.extend(b)
a.sort()
print a
print a[len(a) / 2], len(a) / 2, len(a)