function divisibleTriangleNumber(n) {
  if (n == 1) return 3;
  let counter = 2;
  let triangleNumber = (counter * ++counter) / 2;
  while (noOfFactors(triangleNumber) <= n) {
    triangleNumber = (counter * ++counter) / 2;
  }
  return triangleNumber;
}

function noOfFactors(num) {
  const primeFactors = getPrimeFactors(num);
  let prod = 1;
  for (let p in primeFactors) {
    prod *= primeFactors[p] + 1;
  }
  return prod;
}

function getPrimeFactors(num) {
  let n = num;
  let primes = {};

  let p = 2;
  let sqrt = Math.sqrt(num);

  function checkAndUpdate(inc) {
    if (n % p === 0) {
      const curr = primes[p];
      if (curr) {
        primes[p]++;
      } else {
        primes[p] = 1;
      }
      n /= p;
    } else {
      p += inc;
    }
  }

  while (p === 2 && p <= n) {
    checkAndUpdate(1);
  }

  while (p <= n && p <= sqrt) {
    checkAndUpdate(2);
  }
  if (Object.keys(primes).length === 0) {
    primes[num] = 1;
  } else if (n !== 1) {
    primes[n] = 1;
  }
  return primes;
}

console.log(divisibleTriangleNumber(1));
function divisibleTriangleNumber(n) {
  if (n == 1) return 3;
  let counter = 2;
  let triangleNumber = (counter * ++counter) / 2;
  while (noOfFactors(triangleNumber) <= n) {
    triangleNumber = (counter * ++counter) / 2;
  }
  return triangleNumber;
}

function noOfFactors(num) {
  const primeFactors = getPrimeFactors(num);
  let prod = 1;
  for (let p in primeFactors) {
    prod *= primeFactors[p] + 1;
  }
  return prod;
}

function getPrimeFactors(num) {
  let n = num;
  let primes = {};

  let p = 2;
  let sqrt = Math.sqrt(num);

  function checkAndUpdate(inc) {
    if (n % p === 0) {
      const curr = primes[p];
      if (curr) {
        primes[p]++;
      } else {
        primes[p] = 1;
      }
      n /= p;
    } else {
      p += inc;
    }
  }

  while (p === 2 && p <= n) {
    checkAndUpdate(1);
  }

  while (p <= n && p <= sqrt) {
    checkAndUpdate(2);
  }
  if (Object.keys(primes).length === 0) {
    primes[num] = 1;
  } else if (n !== 1) {
    primes[n] = 1;
  }
  return primes;
}

console.log(divisibleTriangleNumber(1));
function divisibleTriangleNumber(n) {
  if (n == 1) return 3;
  let counter = 2;
  let triangleNumber = (counter * ++counter) / 2;
  while (noOfFactors(triangleNumber) <= n) {
    triangleNumber = (counter * ++counter) / 2;
  }
  return triangleNumber;
}

function noOfFactors(num) {
  const primeFactors = getPrimeFactors(num);
  let prod = 1;
  for (let p in primeFactors) {
    prod *= primeFactors[p] + 1;
  }
  return prod;
}

function getPrimeFactors(num) {
  let n = num;
  let primes = {};

  let p = 2;
  let sqrt = Math.sqrt(num);

  function checkAndUpdate(inc) {
    if (n % p === 0) {
      const curr = primes[p];
      if (curr) {
        primes[p]++;
      } else {
        primes[p] = 1;
      }
      n /= p;
    } else {
      p += inc;
    }
  }

  while (p === 2 && p <= n) {
    checkAndUpdate(1);
  }

  while (p <= n && p <= sqrt) {
    checkAndUpdate(2);
  }
  if (Object.keys(primes).length === 0) {
    primes[num] = 1;
  } else if (n !== 1) {
    primes[n] = 1;
  }
  return primes;
}

console.log(divisibleTriangleNumber(1));
function divisibleTriangleNumber(n) {
  if (n == 1) return 3;
  let counter = 2;
  let triangleNumber = (counter * ++counter) / 2;
  while (noOfFactors(triangleNumber) <= n) {
    triangleNumber = (counter * ++counter) / 2;
  }
  return triangleNumber;
}

function noOfFactors(num) {
  const primeFactors = getPrimeFactors(num);
  let prod = 1;
  for (let p in primeFactors) {
    prod *= primeFactors[p] + 1;
  }
  return prod;
}

function getPrimeFactors(num) {
  let n = num;
  let primes = {};

  let p = 2;
  let sqrt = Math.sqrt(num);

  function checkAndUpdate(inc) {
    if (n % p === 0) {
      const curr = primes[p];
      if (curr) {
        primes[p]++;
      } else {
        primes[p] = 1;
      }
      n /= p;
    } else {
      p += inc;
    }
  }

  while (p === 2 && p <= n) {
    checkAndUpdate(1);
  }

  while (p <= n && p <= sqrt) {
    checkAndUpdate(2);
  }
  if (Object.keys(primes).length === 0) {
    primes[num] = 1;
  } else if (n !== 1) {
    primes[n] = 1;
  }
  return primes;
}

console.log(divisibleTriangleNumber(1));
function divisibleTriangleNumber(n) {
  if (n == 1) return 3;
  let counter = 2;
  let triangleNumber = (counter * ++counter) / 2;
  while (noOfFactors(triangleNumber) <= n) {
    triangleNumber = (counter * ++counter) / 2;
  }
  return triangleNumber;
}

function noOfFactors(num) {
  const primeFactors = getPrimeFactors(num);
  let prod = 1;
  for (let p in primeFactors) {
    prod *= primeFactors[p] + 1;
  }
  return prod;
}

function getPrimeFactors(num) {
  let n = num;
  let primes = {};

  let p = 2;
  let sqrt = Math.sqrt(num);

  function checkAndUpdate(inc) {
    if (n % p === 0) {
      const curr = primes[p];
      if (curr) {
        primes[p]++;
      } else {
        primes[p] = 1;
      }
      n /= p;
    } else {
      p += inc;
    }
  }

  while (p === 2 && p <= n) {
    checkAndUpdate(1);
  }

  while (p <= n && p <= sqrt) {
    checkAndUpdate(2);
  }
  if (Object.keys(primes).length === 0) {
    primes[num] = 1;
  } else if (n !== 1) {
    primes[n] = 1;
  }
  return primes;
}

console.log(divisibleTriangleNumber(500));
