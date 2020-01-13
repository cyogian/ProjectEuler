def latticePathsOld(gridSize):
    """
    This function uses recursion without dynamic programming.
    To calculate the number of possible paths to reach from top-left corner to bottom-right corner.
    It is slow because we traces each possible path from one point in the grid multiple times.
    """
    totalPathCount = 0
    def calcPath(i = 0, j = 0, current = None, prev = None):
        nonlocal totalPathCount
        if not (prev == current): totalPathCount+=1
        if i == gridSize or j == gridSize: return
        calcPath(i + 1, j, "i", current)
        calcPath(i, j + 1, "j", current)
        return
    calcPath()
    return totalPathCount

def latticePaths(gridSize):
    """
    This function uses dynamic programming 
    and calculates the no. of possible paths from any point in a grid only one time.
    There can be mltiple paths that reach the same point again and again.
    So we store the value of pathCount from that particular point in a 2-D array.
    So that if the pathCount for a point is already calcutated.
    We will just fetch it from the array, instead of calculating it again and again.
    This is dynamic programming that leverages spaceComplexity to reduce timeComplexity.
    """
    pathCount = list(list(0 for i in range(gridSize + 1)) for j in range(gridSize + 1))
    def calcPath(i = 0, j = 0):
        nonlocal pathCount
        if i == gridSize or j == gridSize:
            return 1
        if pathCount[i][j] != 0: return pathCount[i][j]
        currentPathCount = calcPath(i + 1, j) + calcPath(i, j + 1)
        pathCount[i][j] = currentPathCount
        return currentPathCount
    return calcPath()


if __name__ == "__main__":
    print(latticePaths(20))