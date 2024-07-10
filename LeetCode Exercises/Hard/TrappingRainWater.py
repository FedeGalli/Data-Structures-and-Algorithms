class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        for i in range(1, len(height) - 1):
            l_elements = height[:i]
            r_elements = height[i + 1:]

            if max(l_elements) != 0:
                l_max = max(height[:i])
                r_max = max(height[i + 1:])

                print(min(l_max, l_max) - height[i] if (min(l_max, l_max) - height[i]) >= 0 else 0)
                trapped_water += min(l_max, r_max) - height[i] if (min(l_max, r_max) - height[i]) >= 0 else 0


        return trapped_water
