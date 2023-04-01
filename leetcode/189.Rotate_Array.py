class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        new_nums = nums
        new_nums[-k:].extend(new_nums[:length-k])
        print(new_nums, nums)
