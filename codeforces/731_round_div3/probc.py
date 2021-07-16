def solve(k,n,m,changes_a, changes_b):
    a_pointer = 0
    b_pointer = 0
    common = []
    file_length = k
    for i in range(n+m):
        if (a_pointer < len(changes_a)) and (changes_a[a_pointer] == 0):
            common.append(changes_a[a_pointer])
            a_pointer+=1
            file_length+=1
        elif (a_pointer < len(changes_a)) and (changes_a[a_pointer] <= file_length):
            common.append(changes_a[a_pointer])
            a_pointer+=1
        elif (b_pointer < len(changes_b)) and (changes_b[b_pointer] == 0):
            common.append(changes_b[b_pointer])
            b_pointer+=1
            file_length+=1
        elif (b_pointer < len(changes_b)) and (changes_b[b_pointer] <= file_length):
            common.append(changes_b[b_pointer])
            b_pointer+=1
        else:
            return -1
    assert len(common) == n+m
    return " ".join([str(x) for x in common])

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input()
        k,n,m=[int(x) for x in input().decode().strip().split(" ")]
        changes_a = [int(x) for x in input().decode().strip().split(" ")]
        changes_b = [int(x) for x in input().decode().strip().split(" ")]

        res = solve(k,n,m,changes_a,changes_b)
        print(res)