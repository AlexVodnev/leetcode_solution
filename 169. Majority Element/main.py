class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = []
        for i in nums:
            if not (i in elem):
                elem.append(i)
        max_cnt = 0
        el = elem[0]
        for i in range(len(elem)):
            cnt = 0
            for j in range(len(nums)):
                if elem[i] == nums[j]:
                    cnt += 1
            if cnt > max_cnt:
                 el = elem[i]
                 max_cnt = cnt
        return el