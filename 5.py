import sys, timeit

def memory_comparison():
    sizes = [1_000, 10_000, 100_000, 1_000_000]
    print(f"{'N':>12} | {'list (байт)':>14} | {'gen (байт)':>12} | {'Ratio':>8}")
    for n in sizes:
        l, g = [x**2 for x in range(n)], (x**2 for x in range(n))
        sl, sg = sys.getsizeof(l), sys.getsizeof(g)
        print(f"{n:>12,} | {sl:>14,} | {sg:>12,} | {sl/sg:>7.0f}×")

def practical_usage():
    words = ["Python", "ітератор", "генератор", "yield", "comprehension", ""]
    print(f"Всі непорожні: {all(len(w) > 0 for w in words)}")
    print(f"CSV: {', '.join(w.upper() for w in words if w)}")
    print(f"Сума квадратів парних (1-100): {sum(x**2 for x in range(1, 101) if x % 2 == 0)}")

if __name__ == "__main__":
    memory_comparison()
    practical_usage()
