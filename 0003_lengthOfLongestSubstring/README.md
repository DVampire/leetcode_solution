#无重复字符的最长子串
![Alt text](https://github.com/DVampire/leetcode_solution/blob/master/0003_lengthOfLongestSubstring/images/1.png)

思路：滑动窗口

万能模板

时间复杂度：O(N)

```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
```

