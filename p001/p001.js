const multisum = number => {
  return [...Array(number).keys()]
    .filter(x => x % 3 == 0 || x % 5 == 0)
    .reduce((acc, v) => acc + v);
};
