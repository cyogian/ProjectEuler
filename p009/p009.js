function specialPythagoreanTriplet(n) {
  // Good luck!
  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j < n - (i + 2); j++) {
      let k = n - (i + j);
      if (i * i + j * j == k * k) return i * j * k;
    }
  }
}

console.log(specialPythagoreanTriplet(1000));
