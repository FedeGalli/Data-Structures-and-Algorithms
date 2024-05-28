class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ""
       
        while(columnNumber > 0):

            result = chr((ord('A') + (columnNumber - 1) % 26)) + result

            columnNumber = int((columnNumber - 1) / 26)


        return result