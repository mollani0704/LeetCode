class Solution(object):
    def twoSum(self, nums, target):
        temp = 0
        result = []

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]
                if(temp == target):
                    result.append(i)
                    result.append(j)
        return result
        