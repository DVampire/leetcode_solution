class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        y = 0
        # 反转一半数字
        while y < x:
            y = y * 10 + x % 10
            x = x // 10

        # 分别是数字长度为偶数和奇数情形
        return y == x or y // 10 == x