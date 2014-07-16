#!/usr/bin/env nodejs
var os = require('os');

var arguments = process.argv.slice(2);
if ( arguments.length == 0 ){
  return console.log("Please tell me what your full name is, try \"js_program Your Full Name\"");
}

console.log("Hello: " + arguments.join(" "));
console.log("You're running on bash by using NODEJS "+ process.version );
console.log( "You're on " + os.type() + " " + os.release() );