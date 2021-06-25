def solve(n, word, questions):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph_dict = {alph[i]:i+1 for i in range(len(alph))}

    tot = 0
    cache= [0]*(len(word)+1)
    for i,a in enumerate(word):
        tot += alph_dict[a]
        cache[i+1] = tot
    for l,r in questions:
        print(cache[r] - cache[l-1])

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,q = [int(x) for x in input().decode().strip().split(" ")]
    word = input().decode().strip()
    questions = []
    for x in range(q):
        l,r = [int(x) for x in input().decode().strip().split(" ")]
        questions.append((l,r))
    res = solve(n,word, questions)
    # print(res)