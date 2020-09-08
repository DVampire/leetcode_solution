class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for index,item in enumerate(nums):
            if target-item in dict:
                return (dict[target-item],index)
            else:
                dict[item] = index
        return []