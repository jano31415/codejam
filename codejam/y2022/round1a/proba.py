import numpy as np

def solve(s):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
        if i != len(s)-1:
            if ord(s[i]) == ord(s[i+1]):
                for j in range(i+1, len(s)):
                    if ord(s[i]) < ord(s[j]):
                        l.append(s[i])
                        break
                    if ord(s[i]) > ord(s[j]):
                        break
            elif ord(s[i]) < ord(s[i+1]):
                l.append(s[i])

    return "".join(l)




if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        s = input()
        res = solve(s)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)

