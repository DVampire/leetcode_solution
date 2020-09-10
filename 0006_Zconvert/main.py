class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        res = ["" for _ in range(numRows)]

        direct = 1
        row = 0
        for c in s:
            res[row] += c
            row = (row + direct) % numRows

            if row == numRows - 1:
                direct = -1
            elif row == 0:
                direct = 1

        return "".join(res)