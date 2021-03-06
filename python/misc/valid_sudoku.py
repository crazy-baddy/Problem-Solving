'''
    https://www.interviewbit.com/problems/valid-sudoku/
'''

def isValidSudoku(A):
    rows = []
    columns = []
    blocks = []

    for i in range(9):
        rows.append([False] * 9)
        columns.append([False] * 9)
        blocks.append([False] * 9)

    h = {
        (0,0) : 0,
        (0,1) : 1,
        (0,2) : 2,
        (1,0) : 3,
        (1,1) : 4,
        (1,2) : 5,
        (2,0) : 6,
        (2,1) : 7,
        (2,2) : 8,
    }
        
    for r in range(9):
        for c in range(9):
            val =  A[r][c]
               
            if val == '.':
                continue
            else:
                val = int(val)-1
                
            if rows[r][val]:
                return 0
            else: 
                rows[r][val] = True 
                
            if columns[c][val]:
                return 0
            else:
                columns[c][val] = True
                
            x = h[(r/3, c/3)]
            if blocks[x][val]:
                return 0
            else:
                blocks[x][val] = True 
    return 1

def test():
    assert isValidSudoku([ "..5.....6", "....14...", ".........", ".....92..", "5....2...", "........3", "...54....", "3.....42.", "...27.6.." ]) == 1

test()
