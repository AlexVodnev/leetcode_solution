class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jc = 0
        i = 0
        while i < len(nums):
            r = i + nums[i]
            jc += 1
            if r < len(nums) - 1:
                max_pos = r + nums[r]
                n = r
                for j in range(r, i, -1):
                    if (nums[j] != 0):
                        if j + nums[j] > max_pos:
                            max_pos = j + nums[j]
                            n = j
            
            else:
                return jc
            if max_pos >= r + nums[r]:
                i = n - 1
            i += 1