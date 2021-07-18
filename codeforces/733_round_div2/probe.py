def solve(s):
    # print(s)
    n=len(s)
    alph="abcdefghijklmnopqrstuvwxyz"
    alph_count = {}#a:0 for a in alph}
    for si in s:
        if si not in alph_count:
            alph_count[si] = 0
        alph_count[si] += 1
    min_count = len(s)+1
    min_a = "a"
    for a in alph_count:
        if alph_count[a] < min_count:
            min_a = a
            min_count = alph_count[a]

    if len(alph_count) == 1:
        return s

    if min_count == 1:
        for z in reversed(alph):
            if z in alph_count:
                if alph_count[z] == 1:
                    first_letter = z
        s = list(s)
        s.remove(first_letter)
        s.sort()
        return first_letter + "".join(s)
    alph_exists = []
    for a in alph:
        if a in alph_count:
            alph_exists.append(a)
    min_a = alph_exists[0]
    s = list(s)
    s.sort()
    if alph_count[min_a] <= (n+2)//2:# n-alph_count >= alph_count-2
        new_s = min_a+min_a
        count = 2
        start = 0
        for i,si in enumerate(s):
            if si == min_a:
                continue
            if count == alph_count[min_a]:
                start = i
                break
            new_s += si+min_a
            count+=1
            start = i+1
        new_s += "".join(s[start:])
        return new_s
    else:
        min_b = alph_exists[1]
        new_s = min_a + min_b
        s.remove(min_a)
        s.remove(min_b)
        if len(alph_exists) > 2:
            min_c = alph_exists[2]
            new_s += min_a*(alph_count[min_a]-1)
            new_s += min_c
            new_s += min_b*(alph_count[min_b]-1)
            new_s += min_c*(alph_count[min_c]-1)
            for a in alph:
                if a in alph_count:
                    if a in [min_a, min_b, min_c]:
                        continue
                    new_s += a*alph_count[a]
            return new_s
        else:
            new_s += min_b * (alph_count[min_b] - 1)
            new_s += min_a * (alph_count[min_a] - 1)
            return new_s






import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())

    for t in range(T):
        s = input().decode().strip()
        res1 = solve(s)
        print(res1)
