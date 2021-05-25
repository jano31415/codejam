def solve(numbers):
    return len(numbers) - numbers.count(min(numbers))


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        numbers = [int(x) for x in input().split(" ")]
        res = solve(numbers)
        print(res, flush=True)