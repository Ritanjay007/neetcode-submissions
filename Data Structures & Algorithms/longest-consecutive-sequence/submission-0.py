class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet =set(nums)
        longest = 0

        for n in nums:
            #check if its start of sequence by checking previous number if it is present in numset
            if n-1 not in numSet:
                streak = 0
                while n+streak in numSet:
                    streak += 1
                longest = max(streak,longest)
        return longest
