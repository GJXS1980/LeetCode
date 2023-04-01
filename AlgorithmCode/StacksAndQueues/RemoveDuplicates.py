#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
删除排序数组中的重复项

Author: GrantLi

要求：
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
由于在某些语言中不能改变数组的长度,所以必须将结果放在数组nums的第一部分。
更规范地说,如果在删除重复项之后有 k 个元素,那么nums的前 k 个元素应该保存最终结果。
将最终结果插入 nums 的前 k 个位置后返回 k 。
不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:
输入:nums = [1,1,2]
输出:2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。
不需要考虑数组中超出新长度后面的元素。

示例 2:
输入:nums = [0,0,1,1,1,2,2,3,3,4]
输出:5, nums = [0,1,2,3,4]
解释:函数应该返回新的长度5,并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。
不需要考虑数组中超出新长度后面的元素。

提示：
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums:nums已按升序排列

"""
import time

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = None
        start = time.time()
        for i in range(0, len(nums)-1):
            if (len(nums)-1) > i:
                while(nums[i] == nums[i+1]):
                    nums.pop(i)
                    print(nums)
                    if (len(nums)-2) < i:
                        break
            else:
                end = time.time()
                print(end - start)
                return len(nums)


# class Solution:
#     def removeDuplicates(self, nums):
#         start = time.time()
#         for i in range(len(nums) - 1, 0, -1):
#             if nums[i] == nums[i - 1]:
#                 del nums[i]
#                 print(nums)
#         end = time.time()
#         print(end - start)
#         return len(nums)


        
if __name__ == '__main__':
    code = Solution()
    num = code.removeDuplicates([1, 2, 3, 4, 4, 4,44,44,55,55,55,55,55,69,94,95,98,98,98,99,99,100,100])
    print(num)



