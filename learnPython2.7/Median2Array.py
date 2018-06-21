
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/#
#
# python 2.7 solution


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:˚
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    print m, n
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        print imin, imax, i, j
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


A = [1, 3,4,5,6]
B = [2]

ret = median(A, B)
print ret
