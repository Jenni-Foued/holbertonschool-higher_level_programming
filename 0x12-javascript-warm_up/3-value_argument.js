#!/usr/bin/node

const arg = process.argv[2];
if (typeof arg === 'undefined') {
  console.log('No argument');
} else {
  console.log(arg);
}
