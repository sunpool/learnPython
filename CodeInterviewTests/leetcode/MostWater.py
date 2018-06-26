# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines
# are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hi = len(height) - 1
        lo = 0
        max_area = -1
        while hi >= lo:
            x_len = hi - lo
            # print(hi, heights[hi], lo, heights[lo])
            print(hi, lo)
            if height[hi] > height[lo]:
                min_height = height[lo]
                lo += 1
            else:
                min_height = height[hi]
                hi -= 1

            area = x_len * min_height
            print(hi, lo, x_len, min_height, area)
            if max_area < area:
                max_area = area

        print(max_area)
        return max_area

    def maxAreaWindx(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hi = len(height) - 1
        lo = 0
        max_area = -1
        max_area_idx = []
        while hi >= lo:
            x_len = hi - lo
            if height[hi] > height[lo]:
                min_height = height[lo]
                # lo += 1
            else:
                min_height = height[hi]
                # hi -= 1

            area = x_len * min_height
            if max_area < area:
                max_area = area
                max_area_idx = [(lo, height[lo]), (hi, height[hi])]
            elif max_area == area:
                max_area_idx.append(((lo, height[lo]), (hi, height[hi])))

            if height[hi] > height[lo]:
                lo += 1
            else:
                hi -= 1
        print(max_area)
        print(max_area_idx)
        return max_area


sol = Solution()
heights = [3, 2, 1, 3]
ret = sol.maxArea(heights)
