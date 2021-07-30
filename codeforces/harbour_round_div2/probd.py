def solve(s,t):

    mod_done = []
    for i, letter in enumerate(s):
        pointer = 0
        if letter == t[0]:
            if i%2 in mod_done:
                continue
            pointer=1
            current = i+1
            last = i

            if pointer == len(t):
                if (len(s) - i) % 2 == 1:
                    return "YES"
                else:
                    continue

            for j in range(current, len(s)):
                if j%2 != last%2:
                    if s[j] == t[pointer]:
                        pointer+=1
                        last = j
                if pointer == len(t):
                    if (len(s)-j)%2 == 1:
                        return "YES"
                    else:
                        break
            mod_done.append(i%2)
    return "NO"




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        s=input().decode().strip()
        t=input().decode().strip()

        res=solve(s,t)
        print(res)