class Solution:
    def hammingWeight(self, n: int) -> int:
        """Editorial Bit Manipulation Solution"""
        sum = 0
        while n:
            sum += 1
            n &= n-1
        return sum
        # """Editorial Loop and Flip solution"""
        # BIT_TOTAL = 32
        # bits = 0
        # mask = 1
        # for i in range(BIT_TOTAL):
        #     if n & mask != 0:
        #         bits += 1
        #     mask <<= 1
        # return bits
