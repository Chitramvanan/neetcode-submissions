class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hash set containing all numbers
        numset = set(nums)
        longest = 0

        for n in numset:
            # Check whether n is the start of a sequence
            if n - 1 not in numset:
                current = n
                length = 1

                # Count the consecutive numbers
                while current + 1 in numset:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
        