def solve(N, K, string):
    if K == 1:
        return 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    len_pal = N//2 + N%2
    res = 0#alphabet.index(string[0]) * K **(len_pal-1)
    mod = 10**9+7
    for i in range(0, len_pal):
        powk = pow(K, len_pal-i-1, mod)
        res += (alphabet.index(string[i]) * powk) % mod
        res = res % mod
        # print(res)
    pal= string[:len_pal] + string[:N//2][::-1]
    # print(pal)
    if pal < string:
        res =(res+1)%mod

    # print(res)
    # print(string)
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N,K = [int(x) for x in input().split(" ")]
        string = input()
        res = solve(N, K, string)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

def solve_stupid():
    res = 0
    len_pal = N//2 + N%2

