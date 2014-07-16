#!/usr/bin/env python
import os
import sys
import platform

def main(argv):

  if len( argv ) == 1:

    print "Please tell me what your full name is, try \"python_program Your Full Name\""

  else:
    argv.pop(0)
    print "Hello: " + " ".join( argv )
    print "You're running on bash by using PYTHON " + sys.version.split(' ')[0]
    print "You're on {} {}".format(platform.system(), platform.release())

if __name__ == "__main__":
  main(sys.argv)
