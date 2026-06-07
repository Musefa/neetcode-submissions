class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set(nums)
        for elem in nums:
            try:
                elems.remove(elem)
            except KeyError:
                return True
        return False