function maximumPathSumI(triangle) {
  // Good luck!
  const cumulativeSum = Array(triangle.length).fill(Array(triangle.length));
  function calcSum(i = 0, j = 0) {
    if (i === triangle.length - 1) {
      return triangle[i][j];
    }
    if (cumulativeSum[i][j]) {
      return cumulativeSum[i][j];
    }
    let left = calcSum(i + 1, j);
    let right = calcSum(i + 1, j + 1);
    return left > right ? triangle[i][j] + left : triangle[i][j] + right;
  }
  return calcSum();
}

const testTriangle = [
  [3, 0, 0, 0],
  [7, 4, 0, 0],
  [2, 4, 6, 0],
  [8, 5, 9, 3]
];

console.log(maximumPathSumI(testTriangle));
