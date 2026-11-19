

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_count = 0

        for num in nums:
            if num == 1:
                counter += 1
                max_count = max(counter, max_count)
            else:
                counter = 0

        return max_count





        