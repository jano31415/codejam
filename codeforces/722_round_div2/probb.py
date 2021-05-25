def solve(numbers):
    if len(numbers) == 1:
        return 1
    numbers_pos = [x for x in numbers if x > 0]
    if len(numbers_pos) == 0:
        return len(numbers)
    res = len(numbers) - len(numbers_pos)
    min_pos = min(numbers_pos)
    numbers_rest = [x for x in numbers if x < min_pos] + [min_pos]
    numbers_rest.sort()
    diff = [0]*(len(numbers_rest)-1)
    for i in range(len(numbers_rest)-1):
        diff[i] = abs(numbers_rest[i+1] - numbers_rest[i])

    if len(diff) == 0 or min(diff) >= min_pos:
        return res+1
    else:
        return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        numbers = [int(x) for x in input().split(" ")]
        res = solve(numbers)
        print(res, flush=True)
