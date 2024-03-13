#!/usr/bin/node
const SquareParent = require('./5-square.js');
class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = !c ? 'X' : c;
    for (let i = 0; i < this.height; ++i) {
      let str = '';
      for (let j = 0; j < this.width; ++j) {
        str = str + c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
