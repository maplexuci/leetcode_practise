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
        for index1 in range(len(self.nums)):
            for index2 in range(index1+1, len(self.nums)):
                if self.nums[index1] + self.nums[index2] == self.target:
                    indices = [index1, index2]
                    break
        return indices

    def run(self):
        nums = json.loads(input('Give a list: '))
        target = int(input('Give a target number: '))
        self.twoSum(nums, target)
        indices = self.judge()
        print(indices)


test = Solution()
test.run()
