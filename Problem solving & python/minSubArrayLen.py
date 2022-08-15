
def minSubArrayLen( target, nums):
    c = 0
    sum = 0
    nums.sort()
    for i in range(1,nums.__len__()):
        sum += nums[-1]
        print("nums[-1]: ", nums[-1])
        print("sum: ", sum)
        nums.pop(-1)
        c += 1
        if sum >= target:
            return c
    if sum<target:
        return 0
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
target = 213
result = minSubArrayLen(target, nums)
print(result)
