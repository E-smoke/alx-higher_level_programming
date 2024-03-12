#!/usr/bin/node
let i, j, str;
let numb = process.argv;
numb = numb[2];
if (!numb || isNaN(parseInt(numb))) {
  console.log('Missing size');
} else {
  numb = Number(numb);
  numb = numb > 0 ? numb : 0;
  i = numb;
  str = 'X';
  for (i; i > 1; --i) {
    str = str + 'X';
  }
  for (j = numb; j > 0; --j) {
    console.log(str);
  }
}
