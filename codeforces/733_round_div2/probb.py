def solve(h,w):
    last = ""
    not_bin = {"0":"1", "1":"0"}
    for i in range(h):
        if i == 0:
            last = "".join(["1" if col %2 == 0 else "0" for col in range(w)])
        elif i == h-1:
            l = []
            for j in range(w):
                if j ==0:
                    l.append(not_bin[last[0]])
                elif j == 1:
                    l.append("0")
                elif j == w-2:
                    if last[-1] == "0":
                        l.append(not_bin[l[-1]])
                    else:
                        l.append("0")
                elif j == w-1:
                    if last[-1] !="1":
                        l.append(not_bin[l[-1]])
                    else:
                        l.append("0")
                else:
                    l.append(not_bin[l[-1]])
            last="".join(l)
        else:
            first = not_bin[last[0]]
            last_dig = not_bin[last[-1]]
            if i == 1:
                if last[1] == "1":
                    first = "0"
                if last[-2] == "1":
                    last_dig = "0"
            last = first+ "0" * (w - 2) + last_dig

        print(last)
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        h,w=[int(x) for x in input().decode().strip().split(" ")]
        solve(h,w)
        print("")