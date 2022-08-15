def fib(n):
    f1 = 0
    f2 = 1

    if (n == 1):
        return f1
    if(n == 2):
        return f1 + f2
    f1 = 1
    f2 = 2
    for i in range(3,n+1):
        f1, f2 = f2, f1+f2
    return f2

def main():
    print(fib(5))

if __name__=="__main__":
    main()