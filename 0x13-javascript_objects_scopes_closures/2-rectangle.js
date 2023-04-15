#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      return {}; // if w or h is not valid, return an empty object
    }
    this.width = w;
    this.height = h;
  }
}
