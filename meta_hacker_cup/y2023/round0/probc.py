def solve(n, apples):
    if len(apples) == 1:
        return 1

    # max number goes with min number
    # 3 cases new number is max, new number is min, else
    # case 1 number is min:
    apples.sort() #ther is a O(n) solution as we only min max first and second but i think its quick
    # enough for 3*10^5
    apple_sum = apples[-2] + apples[0] # second largest, with second smalles as we add a smaller one
    new_apple = apple_sum - apples[-1]
    res1= check_apple_sum(apple_sum, apples, new_apple)
    if res1 > 0:
        return res1
    # case 2,
    # enough for 3*10^5
    apple_sum = apples[-1] + apples[0] # largest, with smallest
    new_apple =  n*apple_sum - sum(apples)
    res2= check_apple_sum(apple_sum, apples, new_apple)
    if res2 > 0:
        return res2

    # case3 apple is max apple
    apple_sum = apples[-1] + apples[1] # second largest, with second smallest
    new_apple =  apple_sum - apples[0]
    res3= check_apple_sum(apple_sum, apples, new_apple)
    if res3 > 0:
        return res3
    return -1

def check_apple_sum(apple_sum, apples, new_apple):
    apple_dict = {}
    # apples.append(new_apple)
    for a in apples:
        if a not in apple_dict:
            apple_dict[a] = 0
        apple_dict[a] += 1
    if new_apple not in apple_dict:
        apple_dict[new_apple] = 0
    apple_dict[new_apple] += 1
    for k in apple_dict:
        if apple_dict[k] != apple_dict.get(apple_sum - k, -1):
            return -1
    return new_apple


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_c.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        n = int(input().decode().strip())
        apples = [int(x) for x in input().decode().strip().split(" ")]
        res1=solve(n, apples)
        print(res1)
        with open("out_c.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")
