#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const len = list.length;
  for (let i = 0; i < len; ++i) {
    count += list[i] === searchElement ? 1 : 0;
  }
  return count;
};
module.exports = exports;
