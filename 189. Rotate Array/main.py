class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            tmp1 = nums[-1]
            del nums[-1]
            nums.insert(0, tmp1)