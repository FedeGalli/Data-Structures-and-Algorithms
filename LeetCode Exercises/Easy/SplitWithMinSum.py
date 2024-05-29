class Solution:

    def clearNumer(self, num: str) -> int:

        number_touched = False

        while(not number_touched):

            if num[0] == "0" and len(num) > 1:
                num = num[1:]
            else:
                number_touched = True


        return int(num)


    def splitNum(self, num: int) -> int:
        
        string_num = str(num)

        string_list = [*string_num]

        num1 = ""
        num2 = ""

        for i in range(len(string_list)):
            
            min_val = min(string_list)
            if i % 2 == 0:
                num1 += min_val

            else:
                num2 += min_val

            string_list.remove(min_val)

        
        return self.clearNumer(num1) + self.clearNumer(num2)