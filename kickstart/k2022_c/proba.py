def solve(s):
    special = {"#", "@", "*", "&"}
    lowercase = 1
    uppercase = 1
    digit = 1
    specialcase = 1
    for si in s:
        if ord(si) >= ord("a") and ord(si) <= ord("z"):
            lowercase = 0
        if ord(si) >= ord("A") and ord(si) <= ord("Z"):
            uppercase = 0
        if ord(si) >= ord("0") and ord(si) <= ord("9"):
            digit = 0
        if si in special:
            specialcase = 0
    if lowercase:
        s += "a"
    if uppercase:
        s += "A"
    if digit:
        s+="1"
    if specialcase:
        s+= "#"
    if len(s) < 7:
        s+= "a" * (7-len(s))
    return s


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n= int(input())
        s= input()
        res = solve(s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)