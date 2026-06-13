from typing import List


class Solution:
    def max_area(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area


heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]

solution = Solution()
print(solution.max_area(heights))