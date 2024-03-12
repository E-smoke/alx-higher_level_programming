#!/usr/bin/node
let argv = process.argv;
argv = argv[2];
if (!argv) {
  console.log('No argument');
} else {
  console.log(argv);
}
