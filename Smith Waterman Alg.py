#Smith Waterman Algorithm Implementation
#Harry McGrory

GAP_PENALTY = -1
MISMATCH_PENALTY = -1000
MATCH_SCORE = 1

def create2DArray(i, j):
    masterArray = []
    for row in range(i):
        subArray = []
        for col in range(j):
            subArray.append(0)
        masterArray.append(subArray)
    return masterArray

def findCellScore(i, j, seq1, seq2, masterArray, pointers):
    if seq1[i-1] == seq2[j-1]:
        addScore = MATCH_SCORE
    else:
        addScore = MISMATCH_PENALTY
    possibleScores = (masterArray[i-1][j-1] + addScore, masterArray[i][j-1] + GAP_PENALTY, masterArray[i-1][j] + GAP_PENALTY)#, 0)
    bestScore = max(possibleScores)
    if possibleScores.index(bestScore) == 0:
        pointers[(i,j)] = (i-1, j-1)
    elif possibleScores.index(bestScore) == 1:
        pointers[(i,j)] = (i, j-1)
    elif possibleScores.index(bestScore) == 2:
        pointers[(i,j)] = (i-1, j)
    else:
        None
    return(bestScore)

def fillMatrix(seq1, seq2, matrix, pointers):
    for row in range(len(seq1)+1):
        for col in range(len(seq2)+1):
            if row == 0 and col == 0:
                matrix[row][col] = 0
            elif row == 0:
                pointers[(row,col)] = (row, col-1)
            elif col == 0:
                pointers[(row,col)] = (row-1, col)
            else:
                matrix[row][col] = findCellScore(row, col, seq1, seq2, matrix, pointers)

def findBestScoreIndex(matrix):
    maxValueX = 0
    maxValueY = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > matrix[maxValueX][maxValueY]:
                maxValueX = row
                maxValueY = col
    return (maxValueX, maxValueY)

def findAllignments(seq1, seq2, matrix, pointers):
    oldX = -1
    oldY = -1
    allignments = ["",""]
    #pointersLocation = findBestScoreIndex(matrix)
    pointersLocation = (len(seq1), len(seq2))
    #while matrix[pointersLocation[0]][pointersLocation[1]] != 0:
    while not (pointersLocation[0] == 0 and pointersLocation[1] == 0):
        if pointers[pointersLocation][0] == pointersLocation[0]:
            allignments[0] += "---"
            allignments[1] += seq2[pointersLocation[1]-1]
        elif pointers[pointersLocation][1] == pointersLocation[1]:
            allignments[1] += "---"
            allignments[0] += seq1[pointersLocation[0]-1]
        else:
            allignments[0] += seq1[pointersLocation[0]-1]
            allignments[1] += seq2[pointersLocation[1]-1]
            oldX = oldX
        oldX = pointersLocation[0]
        oldY = pointersLocation[1]
        pointersLocation = pointers[pointersLocation]
    allignments[0] = allignments[0][::-1]
    allignments[1] = allignments[1][::-1]
    return allignments

seq1 = "GATTACACTACTGATCATCAT"
seq2 = "GATTACACTGGGACTCATCAT"
pointers = {}

seq1 = [seq1[i:i+3] for i in range(0,len(seq1),3)]
seq2 = [seq2[i:i+3] for i in range(0,len(seq2),3)]

matrix = create2DArray(len(seq1)+1, len(seq2)+1)
fillMatrix(seq1, seq2, matrix, pointers)

allignments = findAllignments(seq1, seq2, matrix, pointers)

print(allignments[0])
print(allignments[1])




