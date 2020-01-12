function largeSum(arr) {
  // Good luck!
  let sum = 0;
  for (let i in arr) {
    sum += parseInt(arr[i].substr(0, 11));
  }
  return parseInt(sum.toString().substr(0, 10));
}

const testNums = [
  "37107287533902102798797998220837590246510135740250",
  "46376937677490009712648124896970078050417018260538"
];

console.log(largeSum(testNums));
