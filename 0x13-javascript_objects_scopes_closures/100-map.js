#!/usr/bin/node
const list = require('./100-data.js').list;
const callback = function (l) {
  return l * list.indexOf(l);
};
console.log(list);
console.log(list.map(callback));
