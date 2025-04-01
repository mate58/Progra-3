def Fibonacci(n):
    if n <= 1:
        return n 

    fibo = [0, 1]

    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2]) 

    return fibo[n-1] 


print(Fibonacci(3))
