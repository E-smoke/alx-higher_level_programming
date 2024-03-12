#!/usr/bin/node
let argv = process.argv;
argv = argv[2];
if (!argv || isNaN(parseInt(argv))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv}`);
}
