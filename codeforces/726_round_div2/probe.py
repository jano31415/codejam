def solve(n,k,word):
    cur_best = word[0] * k
    for i in range(2,n+1):
        new_word = (word[:i]* (k//i + 1)) [:k]
        if new_word <= cur_best:
            cur_best = new_word
        if new_word[:i] < cur_best[:i]:
            break
    return cur_best
import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n,k = [int(x) for x in input().decode().strip().split(" ")]
    word = input().decode().strip()
    res = solve(n,k,word)
    print(res)

