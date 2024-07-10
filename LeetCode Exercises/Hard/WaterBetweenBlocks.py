class Solution:
    def trap(self, height: List[int]) -> int:
        left_part = [height[0]]
        right_part = []
        max_water = 0

        for column in height[1:]:
            if left_part[-1] == 0 and max(left_part) != 0:
                if right_part == []:
                    right_part.append(column)
                else:
                    if column >= max(right_part):
                        right_part.append(column)
                    else:
                        max_water += self.calculateWater(left_part, 
                                    right_part)
                        left_part = [right_part[-1], column]
                        right_part = []

                                           
            else:
                if column >= max(left_part):
                    left_part = [column]
                else:
                    left_part.append(column)

            print(str(left_part) + " " + str(right_part))
        

        if left_part != [] and right_part != []:
            max_water += self.calculateWater(left_part, 
                                    right_part)
        
        return max_water

    def calculateWater(self, left_part, right_part):
        l_max = left_part[0]
        r_max = right_part[-1]
        max_water = 0
        current_height = min(l_max, r_max)

        for bar_height in left_part[1:]:
            max_water += current_height - bar_height
        for bar_height in right_part[:-1]:
            max_water += current_height - bar_height
        print(max_water)
        return max_water
                
