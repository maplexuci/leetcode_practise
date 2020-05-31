import json


class Solution:
    """
    A module to return the indices of two elements in a list of numbers.
    The sum of the two elements is a given target number.
    """

    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target

        return nums, target

    def judge(self):
        h = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement not in h:
                h[num] = i
            else:
                return [h[complement], i]

    def find(self):
        nums = json.loads(input('Give a list: '))
        target = int(input('Give a target number: '))
        self.twoSum(nums, target)
        indices = self.judge()
        print(indices)


test = Solution()
test.find()
