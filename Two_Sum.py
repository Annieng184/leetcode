class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums, 0):
            for index1, j in enumerate(nums, 0):
                if i + j == target and index != index1:
                    return index, index1
