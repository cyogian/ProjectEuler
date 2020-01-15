function powerDigitSum(exponent) {
  // Good luck!
  const bigNum = [1];
  for (let i = 1; i <= exponent; i++) {
    let count = bigNum.length + 1;
    let overflow = 0;
    for (let j = 0; j < count; j++) {
      let digit = bigNum[j] || 0;
      digit = 2 * digit + overflow;
      if (digit > 9) {
        digit -= 10;
        overflow = 1;
      } else overflow = 0;
      bigNum[j] = digit;
    }
  }
  return bigNum.reduce((acc, v) => acc + v);
}

console.log(powerDigitSum(15));
