#!/usr/bin/node

function factorial (nb) {
  if (nb === 1 || isNaN(nb)) {
    return 1;
  }
  return (nb * factorial(nb - 1));
}
const arg = process.argv[2];
const fact = factorial(parseInt(arg));
console.log(fact);
