class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums) - k
        nums[:] = nums[length:] + nums[:length]


