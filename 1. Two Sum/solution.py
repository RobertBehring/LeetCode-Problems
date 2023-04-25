class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.bruteTwoSum(nums, target)
        return self.mapTwoSum(nums, target)

    def mapTwoSum(self, nums: list[int], target: int) -> list[int]:
        """Time: O(n) | Space: O(n)"""
        seen = dict()  # hashmap
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i

    def bruteTwoSum(self, nums: list[int], target: int) -> list[int]:
        """Time: O(n^2) | Space: O(1)"""
        list_length = len(nums)

        # Iterate through list one element at a time
        for number in range(list_length - 1):
            # Iterate through list [i+1:n]
            for next_number in range(number + 1, list_length):
                # Check if (i + j) == target
                if nums[number] + nums[next_number] == target:
                    return [number, next_number]