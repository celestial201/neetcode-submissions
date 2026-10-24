from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                d = board[r][c]
                box_idx = (r // 3) * 3 + (c // 3)

                # Three facts about this digit
                keys = (
                    f"row {r}-{d}",
                    f"col {c}-{d}",
                    f"box {box_idx}-{d}"
                )

                for key in keys:
                    if key in seen:
                        return False

                    seen.add(key)

        return True