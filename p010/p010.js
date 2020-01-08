function primeSummation(n) {
  // Good luck!
  const prime = Array(n).fill(true);
  let p = 2;
  while (p * p <= n) {
    if (prime[p]) {
      for (let i = p * p; i <= n + 1; i += p) {
        prime[i] = false;
      }
    }
    p += 1;
  }
  let primeSum = 0;
  for (let p = 2; p < n; p++) {
    if (prime[p]) primeSum += p;
  }
  return primeSum;
}

console.log(primeSummation(17));
