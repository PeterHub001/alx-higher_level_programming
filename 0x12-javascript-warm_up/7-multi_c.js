#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (isNaN(myArgs[0])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parseInt(myArgs[0]) {
    console.log("C is fun");
    i++;
  }
}
