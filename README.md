# Optimizing Lemke's Algorithm in Python

In this repo, I'm working on optimizing a Python implementation of Lemke's algorithm

I have a few different approaches in mind

## Using FLINT's `fmpz` for Big Integers

Python's built-in `int` scales heavily and slows down the process

I replaced every heavily scaling integer with `fmpz` (Fast Multi-Precision Integer) from `flint-python`

FLINT (Fast Library for Number Theory) is highly optimized for big integers, and making this switch alone gave a significant performance boost compared to standard Python ints

I wrote a quick [script](../../tree/testoptimization/tests/test_optimization.py) to test if there are any actual performance improvment
(If there are any mistakes in the testing script, please let me know)

I also check if the final solution and pivot count match the original code

This is represented by the `match` column in the results below

#### Results
<img width="635" height="220" alt="Screenshot benchmark results" src="https://github.com/user-attachments/assets/80c47010-c3bc-46e0-82a9-2825ce67b951" />



These script was run locally on my machine with the following specs:
* **OS:** Windows 11 64-bit
* **Processor:** Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (1.50 GHz)
* **RAM:** 16.0 GB (15.7 GB usable)


## Future Approaches

### Multiprocessing the Pivoting
Every row update during the pivot is independent of the other rows
We should be able to multiprocess the pivoting to handle these updates concurrently

### Modular Arithmetic & CRT
I think we can completely avoid dealing with big numbers during the matrix operations by using modular arithmetic instead
Once the computation is done, we can use the Chinese Remainder Theorem (CRT) to reconstruct the actual numbers
FLINT supports modular arithmetic, so this would make this approach much easier
