

def birthdayCakeCandles(candles):
    # Write your code here
    b = candles.count(max(candles))
    return b
if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))
    print(candles)
    result = birthdayCakeCandles(candles)

