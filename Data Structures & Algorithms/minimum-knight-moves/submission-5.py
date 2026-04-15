class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x

        # Corner cases (don't follow the main formula)
        if (x, y) == (1, 0):
            return 3
        if (x, y) == (2, 2):
            return 4

        # Main formula
        delta = x - y
        if y > delta:
            return delta - 2 * ((delta - y) // 3)
        else:
            return delta - 2 * ((delta - y) // 4)