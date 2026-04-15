class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)  # Use symmetry

        if (x, y) == (0, 0):
            return 0

        # Two queues for bidirectional search
        forward = {(0, 0): 0}
        backward = {(x, y): 0}

        knight_moves = [(2,1), (1,2), (-1,2), (-2,1),
                        (-2,-1), (-1,-2), (1,-2), (2,-1)]

        while forward and backward:
            # Always expand the smaller frontier
            if len(forward) <= len(backward):
                current = forward
                opposite = backward
            else:
                current = backward
                opposite = forward

            next_level = {}
            for (cx, cy), dist in current.items():
                for dx, dy in knight_moves:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in opposite:
                        return dist + 1 + opposite[(nx, ny)]
                    if -2 <= nx <= x + 2 and -2 <= ny <= y + 2:
                        if (nx, ny) not in current:
                            next_level[(nx, ny)] = dist + 1

            if current is forward:
                forward = next_level
            else:
                backward = next_level

        return -1

        