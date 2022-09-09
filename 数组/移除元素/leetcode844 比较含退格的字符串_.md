
错误思路，省题不清： 仍旧用快慢指针，i用来遍历字符串，j用来存储字符串，若当前判断的字符串后面的元素不是#，则覆盖数组,j++,若是#号，则j--
错误:
(1)python中字符串是不可修改的元素，直接逐个修改会报错。可以先将字符串转换为list，再进行修改
(2)python中判断字符串是否相等可以用is/==，判断list是否相等用==
```
class Solution(object):
    def backspaceCompare(self, s, t):
        s_list = list(s)
        t_list = list(t)
        i = 0
        j_1 = 0
        j_2 = 0
        for i in range(0, len(s_list)):

s = "ab#c"
t = "ad#c"
so = Solution()
print(so.backspaceCompare(s,t))
```
思路:从后往前遍历
如果当前是'#'，则skip+1，继续往前遍历;
如果当前不是'#',（1）如果此时skip==0，退出循环,直接和另一个字符串进行比较;
(2)如果此时skip!=0,则i--，skip--,继续下一轮。
错误:考虑有一个字符串已经遍历完的情况,将while i >= 0 and j >= 0 改成 or，其次需要加一个下标的判断条件


```
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = len(s) - 1
        j = len(t) - 1
        skip1 = 0
        skip2 = 0
        while i >=0 or j>=0:
            while i >= 0:
                if s[i] == '#':
                    skip1 += 1
                    i -= 1
                elif s[i] !='#':
                    if skip1 > 0:
                        i -= 1
                        skip1 -= 1
                    else:
                        break
            while j >= 0:
                if t[j] == '#':
                    skip2 += 1
                    j -= 1
                elif t[j] !='#':
                    if skip2 > 0:
                        j -= 1
                        skip2 -= 1
                    else:
                        break
            #判断字符串是否遍历完成为空
            if i < 0 :
                S =""
            else:
                S = s[i]
            if j < 0 :
                T =""
            else:
                T = t[j]
            if S != T:
                return False
            i -= 1
            j -= 1
        return True

s = "aaa###a"
t = "aaaa###a"
solution = Solution()
print(solution.backspaceCompare(s, t))
```
