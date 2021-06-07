def solve(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for a in alphabet:
        if a not in word:
            return a
    for a in alphabet:
        for b in alphabet:
            if a+b not in word:
                return a+b
    for a in alphabet:
        for b in alphabet:
            if a+b not in word:
                return a+b
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:

                if a+b+c not in word:
                    return a+b+c

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        word = input()
        res = solve(word)
        print(res, flush=True)