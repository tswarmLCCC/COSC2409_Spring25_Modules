import sys
import os

# Use a relative path to import the fib module, note that this requries sys and os modules to be imported first
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../lib'))


from fibonacci import fib, fib2
fib(500)