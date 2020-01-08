function specialPythagoreanTriplet(n) {
  // Good luck!
  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j < n - (i + 2); j++) {
      let k = n - (i + j);
      if (i ** 2 + j ** 2 == k ** 2) return i * j * k;
    }
  }
}

console.log(specialPythagoreanTriplet(1000));
