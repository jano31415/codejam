def solve(n,k):
    if n == 1:
        print(0, flush=True)
        res = int(input())
        if res == 1:
            return

    power = 1
    exp = 0
    while power < n:
        power = power * 2
        exp += 1
    counts = [0]*(exp+2)
    not_b = {"0":"1", "1":"0"}
    cur_power = 4
    cur_number = 1
    print(0, flush=True)
    res = int(input())
    if res == 1:
        return
    for i in range(n):
        print(cur_number, flush=True)
        res = int(input())
        if res == 1:
            return
        cur_number = cur_number + 2
        if cur_number > cur_power:
            cur_number = 1
            cur_power = cur_power*2
        # bin_number = "{0:#b}".format(i)[2:]
        # bin_number = "0b" + bin_number.rjust(exp, "0")
        # bin_number = "".join([b if counts[i] %2 == 0 else not_b[b] for i,b in enumerate(bin_number)])
        # for j,b in enumerate(bin_number):
        #     if b == "1":
        #         counts[j] += 1

def solve2(n,k):
    last = 0
    # ln = list(range(n))
    # random.shuffle()
    for i in range(n):
        print(i ^ last, flush=True)
        res = input()
        if res == "1":
            return
        last = i

# import time
# a=time.time()
if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input())
    for t in range(T):
        n,k = [int(x) for x in input().split(" ")]
        last = 0
        for i in range(n):
            print(i ^ last, flush=True)
            res = input()
            if res == "1":
                break
            last = i