# 验证数独中已有的数是否正确，每行不重复，每列不次重复，每个格内不重复。空格为'.'
# Input: [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: True

# 思路：
# 利用哈希表，每行检测一次，每列检测一次，每格检测一次。

class Solution:
    def isVaildSudoku(self, board):
        for i in range(9):
            map = { }
            #print('map = ', map)
            for j in range(9):
                #print('board[i][j] = ', board[i][j])
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in map:
                    map[board[i][j]] = True
                else:
                    return False
                #print(map)

        for j in range(9):
            map = { }
            for i in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in map:
                    map[board[i][j]] = True
                else:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                map = { }
                for si in range(i, i + 3):
                    for sj in range(j, j + 3):
                        if board[si][sj] == '.':
                            continue
                        elif board[si][sj] not in map:
                            map[board[si][sj]] = True
                        else:
                            return False

        return True

if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    s = Solution()
    result = s.isVaildSudoku(board)
    print(result)




