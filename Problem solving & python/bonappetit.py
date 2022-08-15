def bonAppetit(bill, k, b):
    # Write your code here
    bill.pop(k)
    amt = 0
    for i in bill:
        amt += i

    if b==(amt/2):
        print("Bon Appetit")
    else:
        print(abs(b-(amt/2)))
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)