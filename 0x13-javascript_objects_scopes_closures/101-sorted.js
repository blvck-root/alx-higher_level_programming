#!/usr/bin/node
const dict = require('./101-data').dict;
const sort = (obj) => {
  const reverse = {};
  Object.keys(obj).forEach((key) => {
    reverse[obj[key]] = reverse[obj[key]] || [];
    reverse[obj[key]].push(key);
  });
  return reverse;
};
console.log(sort(dict));
