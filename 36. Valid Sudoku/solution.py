class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Example Sudoku Board
        [
            [#,#,#,-,-,-,#,#,#],
            [#,#,#,-,-,-,#,#,#],
            [#,#,#,-,-,-,#,#,#],
            [-,-,-,#,#,#,-,-,-],
            [-,-,-,#,#,#,-,-,-],
            [-,-,-,#,#,#,-,-,-],
            [#,#,#,-,-,-,#,#,#],
            [#,#,#,-,-,-,#,#,#],
            [#,#,#,-,-,-,#,#,#],
        ]
        rows = [0,8]
        cols = [0,8]
        boxs = [0,8]
        """
        length = 9
        blank = "."
        # check rows
        for row in range(length):
            cur_row = []
            cur_col = []
            cur_box = []
            for col in range(length):
                row_val = board[row][col]
                row_not_valid = row_val in cur_row
                col_val = board[col][row]
                col_not_valid = col_val in cur_col
                box_row = col // 3
                box_row += (row // 3) * 3
                box_pos = col % 3
                box_pos += (row % 3) * 3
                box_val = board[box_row][box_pos]
                box_not_valid = box_val in cur_box
                if row_not_valid or col_not_valid or box_not_valid:
                    return False
                if row_val != blank:
                    cur_row.append(row_val)
                if col_val != blank:
                    cur_col.append(col_val)
                if box_val != blank:
                    cur_box.append(box_val)
        return True

