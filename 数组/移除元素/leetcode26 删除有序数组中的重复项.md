
首先，数组是有序的(升序)。仍旧使用快慢双指针法。
遍历数组，除了第一个元素之外，判断每个元素是否等于前一个数组，如果等于，则不做任何处理；如果不等于，则放入j指针下的数组。
可以肯定的是，数组的第一个元素，一定不是重复的，一定会被保留。

```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
s = Solution()
```

