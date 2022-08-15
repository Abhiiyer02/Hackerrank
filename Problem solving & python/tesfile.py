def fib(n, memo = None):
    if memo == None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1 or n ==0:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]

def main():
    n = 1
    sum = 0
    while(fib(n) < 4000000):
        if(fib(n) % 2 == 0):
            sum += fib(n)
        n += 1
    print(sum)


if __name__=="__main__":
    main()



