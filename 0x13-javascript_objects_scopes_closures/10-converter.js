#!/usr/bin/node

exports.converter = function (base) {
  function conv (nb) {
    return nb.toString(base);
  }
  return conv;
};
