#!/usr/bin/node
let x = process.argv;
x = x[2];
if (!x) {
  console.log('Missing number of occurrences');
} else if (isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  x = Number(x);
  x = x > 0 ? x : 0;
  for (x; x > 0; --x) {
    console.log('C is fun');
  }
}
