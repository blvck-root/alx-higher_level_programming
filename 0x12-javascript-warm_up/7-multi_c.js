#!/usr/bin/node

let n = Number.parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  while (n > 0) {
    console.log('C is fun');
    n--;
  }
}
