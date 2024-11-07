import sys
import os

# Add the parent directory of 'src' to sys.path so that we can import the modules in 'lib'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  

from lib.fibonacci import fib

fib(50)