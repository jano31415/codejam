def solve(k,n,air_pos,temperature):
    final_temp = [10**12]*n
    air_pos_set = set(air_pos)
    air_temp = {air_pos[i]:temperature[i] for i in range(k)}
    air_list = [(temperature[i], air_pos[i]) for i in range(k)]
    air_list.sort(key=lambda x:x[0])
    a=min(air_list)
    min_temp = final_temp[0]
    for t,a in air_list:
        if t > min_temp+n:
            break
        for look_left in range(a):
            my_temp = t+look_left
            left_temp = 0
            left_index = a - look_left - 1
            left_temp = final_temp[left_index]
            new_temp = min(left_temp, my_temp)
            min_temp = min(min_temp, new_temp)
            final_temp[left_index] = new_temp
            if look_left > 0:
                if left_index+1 in air_pos_set:
                    if my_temp >= air_temp[left_index+1]:
                        break
                if (left_temp <= my_temp):
                    break

        for look_right in range(n-a+1):
            my_temp = t+look_right
            right_temp = 0
            right_index = a + look_right - 1
            right_temp = final_temp[right_index]
            new_temp = min(right_temp, my_temp)
            min_temp = min(min_temp, new_temp)
            final_temp[right_index] = new_temp
            if look_right > 0:
                if right_index+1 in air_pos_set:
                    if my_temp >= air_temp[right_index+1]:
                        break
                if (right_temp <= my_temp):
                    break

    return " ".join([str(x) for x in final_temp])



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input()
        n,k=[int(x) for x in input().decode().strip().split(" ")]
        air_pos=[int(x) for x in input().decode().strip().split(" ")]
        temperature=[int(x) for x in input().decode().strip().split(" ")]
        res = solve(k,n,air_pos,temperature)
        print(res)
# import random
# k=10**5
# n=3*10**5
# air_pos = list(set([random.randint(0,n) for _ in range(k)]))
# k = len(air_pos)
# temperature = [random.randint(1,10**9) for _ in range(k)]
# import time
# a=time.time()
# solve(k,n,air_pos,temperature)
# b=time.time()
# print(b-a)