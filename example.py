def factorial(n):
    """
    Return the factorial of n, an exact integer >= 0.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    import math
    if math.floor(n) !=  n:
        raise ValueError("n must be exact integer.")
    if n+1 == n:
        raise OverflowError("n too large.")            
    
    result = 1
    factor =2
    while factor <= n:
        result *= factor
        factor += 1

    return result