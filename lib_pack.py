
#Iterative Method

def fibonacci_iterative(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]



#Recursive Method
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series


#Generator Method
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end= '')
        a,b = b, a+b
    print() 

class Trivial:
    pass


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
