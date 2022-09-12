"""
错误思想：保证时间复杂度在O(n)内
  数组中的元素先按绝对值进行排序，再进行平方操作
  采纳快速排序的思想，i指向头，j指向尾。
  从第一个元素i开始判断，
    如果nums[i]<num[j],j--：
    如果nums[i]>=nums[j]，交换两个元素的位置.如果是和一个负数交换的位置，则需要进行i++,如果是和正数，则进行j--
    当i==j时退出循环.
    如果nums全部为正，则不需要进行排序

class Solution(object):
    def sortedSquares(self, nums):
        #如果nums全部为正，则不用再进行排序
        if nums[0] < 0:
            i = 0
            j = len(nums) - 1
            while i < j:
                if abs(nums[i]) >= abs(nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
                    if nums[j] >= 0:
                        j -= 1
                    else:
                        i += 1
                else:
                    j -= 1
        #计算平方
        for i in range(0, len(nums)):
            nums[i] = nums[i]*nums[i]
        return nums
nums = [-4, -1, 0, 3, 10]
s = Solution()
print(s.sortedSquares(nums))
"""
"""
题目只要求时间复杂度为O(n)，没有要求空间复杂度
使用两个指针i和j，每次比较i和j,选择绝对值较大的那个数，将平方逆序放入新数组ans中
注意边界条件的判定，是i<=j，不是i< j
"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        m =  len(nums) - 1
        i = 0
        j = m
        while i <= j:
            if (nums[i]*nums[i]) > (nums[j]*nums[j]):
                ans[m] =  nums[i]*nums[i]
                m -= 1
                i += 1
            else:
                ans[m] =  nums[j]*nums[j]
                m -= 1
                j -= 1
        return ans
nums = [-7, -3, -2, -1]
s = Solution()
print(s.sortedSquares(nums))
