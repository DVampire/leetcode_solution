![Alt text](./images/1.png)

# 思路一：动态规划

对于一个回文串，去除首尾相同的字符，余下部分仍然是个回文串，因此可以考虑使用动态规划求解。

**定义状态**：用P(i,j)表示字符串s的第i到第j个字母组成的子串s[i:j]是否为回文串：
$$
P(i,j) = 
\begin{cases} 
	& True , s[i:j]是回文串 \\
	& False , s[i:j]不是回文串或i>j\\
\end{cases}
$$
**转移方程**：
$$
P(i,j) = P(i+1,j-1) \&\& (S_{i}==S_{j})
$$
也就是说只有s[i+1,j-1]是回文串，并且s的第i和j个字母相同，s[i:j]才是回文串

**边界条件**：

上面的讨论都是建立在s的长度大于2的情况，还要考虑s长度为1或2的情况
$$
\begin{cases} 
 & P(i,i)=True \\
 & P(i,i+1) = (S_{i}==S_{i+1}) \\
\end{cases}
$$

```python
class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len] 
```

**时间复杂度**：
$$
O(n^{2})
$$
动态规划状态数是O(n^2)，转移时间是O(1)

**空间复杂度**：
$$
O(n^{2})
$$


# 思路二：中心扩展法

从思路一可以发现每一种状态转移都是唯一的，我们可以从每一种边界情况开始扩展，也可以得到所有状态对应的答案。

边界情况是子串长度为1或2的情况。枚举每一种边界情况，并对对应子串不断向外扩展，如果两边字母字母相同可以继续向外扩展，如果不同就停止扩展。

```python
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
```

**时间复杂度**：
$$
O(n^{2})
$$
长度为1和2的回文中心有n和n-1个，每个回文中心最多向外扩展n次

**空间复杂度**：
$$
O(1)
$$

# 思路三：Manacher算法

定义新概念**臂长**，回文串长度为2*length+1，那么臂长是length

```python
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

```

**时间复杂度**：
$$
O(n)
$$
对于每个位置，扩展要么从当前的最右臂长开始，要么只会进行一步，而最右臂长最多走n步骤

**空间复杂度**：
$$
O(n)
$$
需要n个空间记录每个位置臂长