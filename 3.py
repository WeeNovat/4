import itertools

def arithmetic_progression(start: float, step: float):
    curr = start
    while True:
        yield curr
        curr += step

def geometric_progression(start: float, ratio: float, limit: float = float("inf")):
    curr = start
    while curr <= limit:
        yield curr
        curr *= ratio

def fibonacci(n: int | None = None):
    a, b = 0, 1
    count = 0
    while n is None or count < n:
        yield a
        a, b = b, a + b
        count += 1

def collatz_sequence(n: int):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

def main():
    print(f"Арифметична (2, 3): {list(itertools.islice(arithmetic_progression(2, 3), 10))}")
    print(f"Геометрична (до 1000): {list(geometric_progression(1, 2, 1000))}")
    
    for fib_num in fibonacci():
        if fib_num > 10000:
            print(f"Перше Фібоначчі > 10000: {fib_num}")
            break

    nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
    print(f"Розгортання: {list(flatten(nested))}")

if __name__ == "__main__":
    main()
