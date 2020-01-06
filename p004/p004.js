const isPalindrome = s => {
  let palindrome = true,
    lengthS = s.length;
  for (let i = 0; i <= lengthS / 2; i++) {
    if (s[i] !== s[lengthS - i - 1]) {
      palindrome = false;
      break;
    }
  }
  return palindrome;
};
function largestPalindromeProduct(n) {
  // Good luck!
  let maxN = parseInt("9".repeat(n));
  let minN = parseInt("1".concat("0".repeat(n - 1)));
  let s = 0;
  for (let i = maxN; i > minN; i--) {
    for (let j = i; j > minN; j--) {
      let product = i * j;
      if (isPalindrome(product.toString())) {
        if (product > s) s = product;
        break;
      }
    }
  }
  return s;
}

largestPalindromeProduct(3);
