import sys

from crt_lib import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])