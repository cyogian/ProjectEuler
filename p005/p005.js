const gcd = (a, b) => {
  let numerator, denominator;
  if (a > b) {
    numerator = a;
    denominator = b;
  } else {
    numerator = b;
    denominator = a;
  }
  let remainder = numerator % denominator;
  while (remainder != 0) {
    numerator = denominator;
    denominator = remainder;
    remainder = numerator % denominator;
  }
  return denominator;
};

const lcm = (a, b) => {
  return Math.floor((a * b) / gcd(a, b));
};

const lowestCommonMultiple = n =>
  [...Array(n).keys()].map(x => x + 1).reduce((acc, v) => lcm(acc, v));
