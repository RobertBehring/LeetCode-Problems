class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list()

        sorted1 = sorted(nums1)
        m = len(sorted1) - 1
        sorted2 = sorted(nums2)
        n = len(sorted2) - 1

        while m >= 0 and n >= 0:
            if sorted1[m] > sorted2[n]:
                m -= 1
            elif sorted1[m] < sorted2[n]:
                n -= 1
            else:
                intersection.append(sorted1[m])
                m -= 1
                n -= 1
        return intersection
