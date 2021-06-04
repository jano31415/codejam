def solve(N, palindrome):
    count1 = palindrome.count("0")
    if count1 == 0:
        return "DRAW"
    if len(palindrome) % 2 == 0:
        return "BOB"
    if palindrome[len(palindrome)//2] == "0":
        if count1 < 3:
            return "BOB"
        return "ALICE"
    return "BOB"

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        palindrome = input()
        res = solve(N, palindrome)
        print(str(res), flush=True)