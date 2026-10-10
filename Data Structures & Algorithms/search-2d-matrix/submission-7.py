class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            coords = getCoords(mid, len(matrix), len(matrix[0]))
            row, col = coords[0], coords[1]

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False

def getCoords(index: int, rows: int, cols: int) -> List[int]:
    r = index // cols
    c = index % cols
    return [r, c]