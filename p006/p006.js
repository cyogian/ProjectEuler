function sumSquareDifference(n) {
  // Good luck!
  let squareOfSum = ((n * (n + 1)) / 2) ** 2,
    sumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6;
  return squareOfSum - sumOfSquares;
}

sumSquareDifference(100);
