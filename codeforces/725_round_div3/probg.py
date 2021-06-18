def solve(x,y,a,b):
    if x > y:
        swap = x
        x = y
        y = swap
    # x <= y
    if a > b:
        swap = a
        a = b
        b = a
    # a <= b
    # if x//a >= y//b:
    #     return y//b


    # x red , y blue
    # box1 a red ,b blue
    nr_boxes = (x+y) // (a+b)
    # nr_boxes = b1+b2
    # a*b1 + b*b2 = x
    # a*b2 + b*b1 = y
    # a*(b1-b2) + b*(b2-b1) = x-y
    # (a-b)*(nr_boxes-2*b2)  = x-y
    if a!=b:
        b2 = (nr_boxes-(x-y)/(a-b))/2
        b1 = nr_boxes - b2
    else:
        b1=b2=0

    return max( min(x//a, y//b), min(x//b, y//a), int(b1)+nr_boxes-int(b1))




import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        x,y,a,b= [int(x) for x in input().decode().strip().split(" ")]
        res = solve(x,y,a,b)
        print(res)