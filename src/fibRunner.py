import sys
import os

# Use a relative path to import the fib module, note that this requries sys and os modules to be imported first
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../lib'))

import fibonacci as fibo

def main():
    n = 10  # Example value
    print(f"Fibonacci sequence up to {n}:")
    for i in range(n):
        print(fibo.fib(i))

if __name__ == "__main__":
    main()