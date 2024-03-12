#!/usr/bin/node
const argv = process.argv;
const numb = argv.length;
if (numb < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
