class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = [nums[0]]
        rpt = 0
        for i in range(1, len(nums)):
            if nums[i] == tmp[-1]:
                rpt +=1
            else:
                rpt = 0
            if rpt < 2:
                tmp.append(nums[i])
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)