class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.recFloodFill(image, sr, sc, color)

        return image

    def recFloodFill(self, image, sr, sc, color):
        cur_color = image[sr][sc]
        if cur_color == color:
            return

        image[sr][sc] = color

        # recursively color all surrounding blocks
        above = sr - 1
        below = sr + 1
        left = sc - 1
        right = sc + 1
        # above
        if above >= 0 and image[above][sc] == cur_color:
            self.recFloodFill(image, above, sc, color)
        # below
        if below < len(image) and image[below][sc] == cur_color:
            self.recFloodFill(image, below, sc, color)
        # left
        if left >= 0 and image[sr][left] == cur_color:
            self.recFloodFill(image, sr, left, color)
        # right
        if right < len(image[0]) and image[sr][right] == cur_color:
            self.recFloodFill(image, sr, right, color)
