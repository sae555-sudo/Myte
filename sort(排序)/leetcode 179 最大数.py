

"""
转换成字符串，按字符串长度进行存储，然后分别进行排序
"""
import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        flag = 0
        for val in nums:
            if val != 0:
                flag = 1
                break
        if flag == 1: 
            result = ""  #存储最终结果
            nums = list(map(str, nums)) #将int转换为str list
            def cmp(x, y):  #排序规则
                if x+y > y+x:
                    return 1
                else:
                    return -1
            nums.sort(key=functools.cmp_to_key(cmp), reverse= True)
            result = result.join(nums)
        else:
            result = "0"
        return result

nums = [3,30,34,5,9] 
s = Solution()
print(s.largestNumber(nums))
