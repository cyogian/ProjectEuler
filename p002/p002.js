const fib = number => {
  let t1 = 1,
    t2 = 2,
    sum = 0;
  for (let i = 0; i < number; i++) {
    if (t1 % 2 == 0) {
      sum += t1;
    }
    let temp = t1;
    t1 = t2;
    t2 += t1;
  }
  return sum;
};
