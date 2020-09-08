from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #使用defaultdict，当key不在时可以初始化值为0
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0

        while end < len(s):
            #尾指针往后遍历，如果出现了重复字符，就对计数器加一，表明出现了重复
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1

            #counter>0说明有重复字符
            while counter > 0:
                #从头指针往尾指针遍历，出现重复就对counter-1，头指针往后移
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len