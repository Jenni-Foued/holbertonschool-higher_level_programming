#!/usr/bin/node

const arg = process.argv[2];
const argint = parseInt(arg);
if (isNaN(argint)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argint);
}
