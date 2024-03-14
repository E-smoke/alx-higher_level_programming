#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  const len = list.length;
  for (let i = len - 1; i > -1; --i) {
    rev.push(list[i]);
  }
  return rev;
};
module.exports = exports;
