function sumFactorialDigits(n) {
  // Good luck!
  const bigNum = [1];
  for (let i = 2; i <= n; i++) {
    let count = bigNum.length;
    let overflow = 0;
    for (let j = 0; j < count; j++) {
      let digit = bigNum[j];
      digit = digit * i + overflow;
      overflow = Math.floor(digit / 10);
      bigNum[j] = digit % 10;
    }
    while (overflow > 0) {
      bigNum.push(overflow % 10);
      overflow = Math.floor(overflow / 10);
    }
  }
  return bigNum.reduce((acc, v) => acc + v);
}

console.log(sumFactorialDigits(100));
