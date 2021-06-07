def solve(numbers):
    sorted_nr = numbers[:]
    sorted_nr.sort()
    highest = [sorted_nr[2], sorted_nr[3]]
    if (max(numbers[0], numbers[1])) in highest and (max(numbers[2], numbers[3]) in highest):
        return "YES"
    return "NO"


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        numbers = [int(x) for x in input().split(" ")]
        res = solve(numbers)
        print(str(res), flush=True)