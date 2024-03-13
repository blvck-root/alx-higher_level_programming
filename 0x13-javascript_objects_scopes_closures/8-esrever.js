#!/usr/bin/node
exports.esrever = function (list) {
  let revArray = [];

  for (let element of list) {
    revArray.unshift(element);
  }

  return revArray;
}
