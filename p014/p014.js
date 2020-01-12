function sequenceLength(num) {
  let length = 1;
  while (num >= 1) {
    if (num === 1) break;
    if (num % 2 == 0) num /= 2;
    else num = 3 * num + 1;
    length++;
  }
  return length;
}

function longestCollatzSequence(limit) {
  // Good luck!
  let longestSequenceLength = 1;
  let startingNum = 1;
  for (let i = 2; i <= limit; i++) {
    let currentSequenceLength = sequenceLength(i);
    if (currentSequenceLength > longestSequenceLength) {
      longestSequenceLength = currentSequenceLength;
      startingNum = i;
    }
  }
  return startingNum;
}

console.log(longestCollatzSequence(46500));
