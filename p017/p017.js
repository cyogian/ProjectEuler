function numberLetterCounts(limit) {
  // Good luck!
  const zeroTo19 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8];
  const twentyTo90 = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6];
  const hundred = 7;
  const thousand = 8;
  const thousandAnd = 11;
  const hundredAnd = 10;
  function letterCount(num) {
    if (num <= 19) {
      return zeroTo19[num];
    }
    if (num < 100) {
      return twentyTo90[Math.floor(num / 10)] + zeroTo19[num % 10];
    }
    if (num < 1000) {
      let hundredth = num % 100;
      if (hundredth == 0) {
        return zeroTo19[Math.floor(num / 100)] + hundred;
      }
      return (
        zeroTo19[Math.floor(num / 100)] + hundredAnd + letterCount(hundredth)
      );
    }
    let thousandth = num % 1000;
    if (thousandth == 0) {
      return zeroTo19[Math.floor(num / 1000)] + thousand;
    }
    if (thousandth >= 100) {
      return (
        zeroTo19[Math.floor(num / 1000)] + thousand + letterCount(thousandth)
      );
    }
    return (
      zeroTo19[Math.floor(num / 1000)] + thousandAnd + letterCount(thousandth)
    );
  }
  let totalCount = 0;
  for (let i = 1; i <= limit; i++) {
    totalCount += letterCount(i);
  }
  return totalCount;
}

console.log(numberLetterCounts(1000));
