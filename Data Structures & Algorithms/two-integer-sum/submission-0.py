class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #Empty hashmap to store the element
       prevMap = {}
       #Iterate each elements
       for i,n in enumerate(nums):
            #caluclate diff
            difference = target - n
            #if need value is exist in hash map
            if difference in prevMap:
                return [prevMap[difference], i]
            #otherwise store it in preve map
            prevMap[n] = i