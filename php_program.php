#!/usr/bin/env php
<?php

if ( count($argv) == 1 ){
  echo "Please tell me what your full name is, try \"php_program Your Full Name\"\n";
}
else{
  array_shift($argv);
  echo "Hello: " . implode(" ", $argv) . "\n";
  echo "You're running on bash by using PHP " . phpversion() . "\n";
  echo "You're on ". php_uname('s') . " " . php_uname('r') . "\n";

}