思路1：和leetcode27 思路类似，都是移除元素，只不过之前是移除指定元素，这次是移除零。
      仍旧使用快慢双指针法，先将非0元素移到前面，同时统计元素0的个数，再将元素0放到数组后面
```
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums
        i = 0
        j = 0
        sum = 0  #用来统计数组nums中0的个数
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                sum += 1
        nums[j:] = [0] * sum
        return nums
```
思路2： 仍然采用两个指针，一个指针i仍然用来遍历数组，一个数组j用来记录。每次进行交换
```
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums
        i = 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
nums = [0,1,0,3,12]
s = Solution()
print(s.moveZeroes(nums))
```
