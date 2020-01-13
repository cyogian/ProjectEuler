function latticePathsOld(gridSize) {
  // Good luck!
  // Without Dynamic Programming, therefore slow.
  let totalPathCount = 0;
  function calcPath(i = 0, j = 0, current, prev) {
    if (!(prev == current)) totalPathCount++;
    if (i === gridSize || j === gridSize) {
      return;
    }
    calcPath(i + 1, j, "i", current);
    calcPath(i, j + 1, "j", current);
    return;
  }
  calcPath();
  return totalPathCount;
}

function latticePaths(gridSize) {
  // Good luck!
  const pathCount = Array(gridSize + 1)
    .fill()
    .map(() => Array(gridSize + 1));
  function calcPath(i = 0, j = 0) {
    if (i === gridSize || j === gridSize) return 1;
    if (pathCount[i][j]) return pathCount[i][j];
    let currentPathCount = calcPath(i + 1, j) + calcPath(i, j + 1);
    pathCount[i][j] = currentPathCount;
    return currentPathCount;
  }
  return calcPath();
}

console.log(latticePaths(1));
