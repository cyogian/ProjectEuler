function nthPrime(n) {
  // Good luck!
  const primeList = [];
  let i = 2,
    j = 1;
  while (j <= n) {
    let isPrime = true;
    for (let k = 0; k < primeList.length; k++) {
      if (i % primeList[k] == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primeList.push(i);
      j += 1;
    }
    i += 1;
  }
  return primeList[primeList.length - 1];
}

nthPrime(10001);
