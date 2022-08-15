
def solve(n,arr):
    max_position = [0]*(n+1)
    for i,a in enumerate(arr):
        max_position[a] = max(max_position[a],i)

    index = n-1
    last = arr[index]
    max_index=-1
    for a in arr[::-1]:
        if a > last:
            max_index = index
            break
        last = arr[index]
        index-=1
    if max_index == -1:
        return 0
    delete = set()
    for i in range(n):
        if i > max_index:
            break
        delete.add(arr[i])
        max_index = max(max_index, max_position[arr[i]])

    return len(delete)

    # n_to_pos = {}
    # for i,a in enumerate(arr):
    #     if a not in n_to_pos:
    #         n_to_pos[a] = []
    #     n_to_pos[a].append(i)
    # last = arr[0]
    # last_i = 0
    # res=0
    # for i,a in enumerate(arr):
    #     if a < last:
    #         for j in range(last_i,i-1):
    #             aval =arr[j]
    #             if aval != 0:
    #                 for k in n_to_pos[aval]:
    #                     arr[k] = 0
    #                 n_to_pos[aval] = []
    #                 res+=1
    #         last_i = i
    #         last = arr[i]



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]
        res=solve(n,arr)
        print(res)

