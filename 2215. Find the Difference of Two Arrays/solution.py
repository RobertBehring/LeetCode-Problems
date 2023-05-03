class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert to set to do logic arithmetic
        set1 = set(nums1)
        set2 = set(nums2)
        # calculate complements for each set
        com1 = set1 - set2
        com2 = set2 - set1
        return [list(com1), list(com2)]
