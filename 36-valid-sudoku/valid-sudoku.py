class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid = True
        for i in range(len(board)):
            rowMap = {}
            colMap = {}
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                else:
                    rowMap[board[i][j]] = rowMap.get(board[i][j],0)+1
            # print(rowMap)
            for val in rowMap.values():
                if val>1:
                    is_valid=False
            if not is_valid:
                break
        if is_valid:
            # process col wise
            for i in range(len(board[0])):
                colMap = {}
                for j in range(len(board)):
                    if board[j][i]=='.':
                        continue
                    else:
                        colMap[board[j][i]] = colMap.get(board[j][i],0)+1
                print(colMap)
                for val in colMap.values():
                    if val>1:
                        is_valid=False
                if not is_valid:
                    break
        if is_valid:
            # process sub-matrix wise
            rowSt=0
            colSt=0
            for x in range(9):
                mp = {}
                for i in range(rowSt,rowSt+3):
                    for j in range(colSt,colSt+3):
                        # print(i,j)
                        if board[i][j]=='.':
                            continue
                        else:
                            mp[board[i][j]] = mp.get(board[i][j],0)+1
                    # print(mp)
                    for val in mp.values():
                        if val>1:
                            is_valid=False
                    if not is_valid:
                        break
                if not is_valid:
                    break
                colSt+=3
                x+=1
                if x%3==0:
                    rowSt+=3
                    colSt=0
        return is_valid