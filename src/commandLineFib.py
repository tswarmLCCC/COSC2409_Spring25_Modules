import sys
import os

# Use a relative path to import the fib module, note that this requries sys and os modules to be imported first
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../lib'))

import fibonacci as fibo


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python commandLineFib.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num <= 0:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer.")
        sys.exit(1)
    
    fib_sequence = fibo.fib(num)
    print(f"Fibonacci sequence up to {num} terms: {fib_sequence}")
