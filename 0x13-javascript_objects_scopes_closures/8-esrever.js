#!/usr/bin/node
exports.esrever = function (list) {
  const revArray = [];

  for (const element of list) {
    revArray.unshift(element);
  }

  return revArray;
};
