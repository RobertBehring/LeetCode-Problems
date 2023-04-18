class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        cur_row = 1

        while cur_row < numRows:
            prev_row = cur_row-1
            row = [1]
            for i in range(len(pascal[prev_row])):
                if i == len(pascal[prev_row])-1:
                    row.append(1)
                else:
                    row.append(pascal[prev_row][i] + pascal[prev_row][i+1])

            pascal.append(row)
            cur_row += 1

        return pascal
