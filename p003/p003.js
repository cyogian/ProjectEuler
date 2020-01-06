function largestPrimeFactor(number) {
  // Good luck!
  let primeList = [],
    maxPrimeFactor = 0,
    i = 2;
  while (i <= number) {
    let isPrime = true;
    for (let j = 0; j < primeList.length; j++) {
      if (i % primeList[j] == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primeList.push(i);
      if (number % i == 0) maxPrimeFactor = i;
      while (number % i == 0) number = number / i;
    }
    i++;
  }
  return maxPrimeFactor ? maxPrimeFactor : number;
}

largestPrimeFactor(600851475143);
