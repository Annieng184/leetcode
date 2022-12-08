class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return min(result, key=result.get)
