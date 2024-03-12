#!/usr/bin/node
let numb = process.argv;
numb = numb.length;
if (numb < 3) {
  console.log('No argument');
} else if (numb === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
