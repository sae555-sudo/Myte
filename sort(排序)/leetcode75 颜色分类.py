class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        统计nums中0 1 2的个数，然后分别赋值
        """
        color_num = [0, 0, 0]
        for i in nums:
            color_num[i] = color_num[i] + 1
        i = 0
        for index,value in enumerate(color_num):
            nums[i : i+value] = [index] * value
            i = i + value
        return nums

nums = [2,0,2,1,1,0]
s = Solution()
nums = s.sortColors(nums)
print(nums)