#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. 
#Note that you must do this in-place without making a copy of the array.

#Approach 1:
class Solution:
  def moveZeroes(self, nums: List[int]) -> None: 
    zero_size = nums.count(0)
    nums.delete(0)
    nums = (nums + ([0] * zero_size ))
  

#Approach 2:
class Solution:
  def moveZeroes(self, nums: List[int]) -> None: 
    n = nums.count(0)
    for i in range(n):
      nums.remove(0)
      nums.append(0)
