class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in idx_map and idx_map[diff]!=idx:
                return [idx_map[diff], idx]
            idx_map[val] = idx
