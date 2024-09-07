from typing import List

'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5]
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = int('inf')
        middle = int('inf')
        
        for num in nums:
          if num <= smallest:
              smallest = num
          elif num <= middle:
              middle = num
          elif num > middle:
              return True 
        return False
            
'''
Notes: Need to think about how we would actually track the i<j<k so we can have smallest and middle and assign then to inifnity and then compare them
with each num in the list. This way we compare adn get the lowest, we compare and get middle and then lastly we compare with greater than middle and 
if it's found return True else False
'''