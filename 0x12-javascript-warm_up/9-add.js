#!/usr/bin/node
function add (a, b) {
  if (!a || !b) {
    console.log('NaN');
  }
  console.log(a + b);
}
const argv = process.argv;
const f = argv[2];
const s = argv[3];
if (!f || !s) {
  console.log('NaN');
} else {
  add(Number(f), Number(s));
}
