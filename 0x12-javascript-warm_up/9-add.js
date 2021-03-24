#!/usr/bin/node

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}

const nb1 = process.argv[2];
const nb2 = process.argv[3];
const sum = add(nb1, nb2);

console.log(sum);
