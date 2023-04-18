class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        given_size = sum([len(x) for x in mat])
        if given_size != (r * c):
            return mat

        reshape_array = [[0 for x in range(c)] for y in range(r)]

        cur_row = 0
        cur_col = 0

        for nums in mat:
            for num in nums:
                if cur_col == c:
                    cur_row += 1
                    cur_col = 0
                reshape_array[cur_row][cur_col] = num
                cur_col += 1

        return reshape_array
