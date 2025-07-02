def twoSum(numbers, target):
    L = 0
    R = len(numbers) - 1

    while L <= R:
        sum = numbers[L] + numbers[R]
        if sum == target:
            return [L+1, R+1]
        if sum < target:
            L += 1
        if sum > target:
            R -= 1
    return False


print(twoSum([2,7,11,15], 9))