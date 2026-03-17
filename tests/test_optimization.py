import time
import numpy as np
from src.lemke.lemke import tableau, lcp 
from src.lemke.optimizedlemke import tableau as optimizedtableau
import fractions


def generate_lcp_input(n):
    q = np.random.randint(-20, -1, size=n).astype(float)
    B = np.random.randint(-5, 5, size=(n, n)).astype(float)
    M = B @ B.T + np.eye(n) * n

    Mqd = lcp(n)
    Mqd.M = [[fractions.Fraction(int(M[i][j])) for j in range(n)] for i in range(n)]
    Mqd.q = [fractions.Fraction(int(q[i])) for i in range(n)]
    Mqd.d = [fractions.Fraction(1)] * n

    return Mqd


def run_test():
    N = [100,250,400,500,1000]
    
    print(f"{'n':<5} | {'Original(s)':<12} | {'Optimized(s)':<12} | {'Match?':<10}")
    print("-" * 45)

    for n in N:
        Mqd = generate_lcp_input(n)
        
        original_tableau = tableau(Mqd)
        start = time.perf_counter()
        original_tableau.runlemke(silent=True)
        end = time.perf_counter()
        original_time = end - start

        optimized_tableau = optimizedtableau(Mqd)
        start = time.perf_counter()
        optimized_tableau.runlemke(silent=True)
        end = time.perf_counter()
        optimized_time = end - start

        is_correct = (original_tableau.solution == optimized_tableau.solution) and (original_tableau.pivotcount == optimized_tableau.pivotcount)
        match_status = "ok" if is_correct else "fail"
        
        print(f"{n:<5} | {original_time:<12.6f} | {optimized_time:<12.6f} | {match_status:<10}")


if __name__ == "__main__":
    run_test()