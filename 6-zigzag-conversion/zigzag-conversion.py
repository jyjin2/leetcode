class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # trivial cases
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        # curr = start at row 0 (top)
        # direction start moving down the rows
        curr, direction = 0, 1

        for ch in s:
            rows[curr] += ch
            if curr == 0:
                direction = 1   # force direct downward
            # at the bottom row (numRows-1)
            elif curr == numRows - 1:
                direction = -1  # force direct upward
            curr += direction
        return ''.join(rows)