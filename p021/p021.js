function sumOfDivisors(n) {
  if (n == 1) return 0;
  let sum = 1;
  let sqrt = Math.sqrt(n);
  for (let i = 2; i < sqrt; i++) {
    if (n % i == 0) {
      sum += i + n / i;
    }
  }
  if (Math.floor(sqrt) === sqrt) {
    sum += sqrt;
  }
  return sum;
}

function sumAmicableNum(n) {
  // Good luck!
  const d = Array(n);
  let sum = 0;
  for (let i = 1; i < n; i++) {
    d[i] = sumOfDivisors(i);
  }
  for (let i = 2; i < n; i++) {
    let dSum = d[i];
    if (d[dSum] === i && i !== dSum) sum += dSum;
  }
  return sum;
}
console.log(sumAmicableNum(5000));
