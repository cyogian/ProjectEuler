function getDay(date) {
  const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let noOfDays = 0;
  for (let year = 1900; year < date.year; year++) {
    if (year % 400 === 0) {
      noOfDays += 366;
    } else if (year % 4 === 0 && year % 100 !== 0) {
      noOfDays += 366;
    } else {
      noOfDays += 365;
    }
  }
  for (let month = 0; month < date.month; month++) {
    noOfDays += daysInMonth[month];
  }
  if (date.month > 1) {
    if (date.year % 400 === 0) {
      noOfDays += 1;
    } else if (date.year % 4 === 0 && date.year % 100 !== 0) {
      noOfDays += 1;
    }
  }
  noOfDays += date.day;
  return noOfDays % 7;
}
function countingSundays(firstYear, lastYear) {
  // Good luck!
  let sundays = 0;
  const day = 1;
  for (let year = firstYear; year <= lastYear; year++) {
    for (let month = 0; month <= 11; month++) {
      let date = { year, month, day };
      if (getDay(date) === 0) {
        sundays++;
      }
    }
  }
  return sundays;
}
console.log(countingSundays(1901, 2000));
