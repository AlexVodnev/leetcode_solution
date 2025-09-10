class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            r = i + nums[i]
            if r < len(nums) - 1 and r != i:
                max_pos = r + nums[r]
                n = r
                for j in range(r, i, -1):
                    if (nums[j] != 0):
                        if j + nums[j] > max_pos:
                            max_pos = j + nums[j]
                            n = j
            elif r < len(nums) - 1 and r == i:
                return False
            else:
                return True
            if max_pos >= r + nums[r]:
                i = n - 1
            i += 1