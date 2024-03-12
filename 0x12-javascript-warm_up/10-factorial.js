#!/usr/bin/node
function factorial () {
  let argv = process.argv;
  argv = argv[2];
  if (!argv) {
    console.log('1');
    return;
  }
  argv = Number(argv);
  if (!argv || argv === 0) {
    console.log('1');
    return;
  }
  argv = argv > 0 ? argv : 0;
  let fac = 1;
  for (argv; argv > 0; --argv) {
    fac = fac * argv;
  }
  console.log(`${fac}`);
  return fac;
}
factorial();
