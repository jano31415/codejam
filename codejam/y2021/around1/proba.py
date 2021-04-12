def solve(N, integers):
    curr_min = integers[0]
    count = 0
    for i, x in enumerate(integers[1:]):
        if x > curr_min:
            curr_min = x
            continue
        if x == curr_min:
            count+=1
            curr_min = 10*x
            continue
        while x < curr_min:
            str_x = str(x)
            str_curr_min = str(curr_min)
            if str_x == str(curr_min)[:len(str_x)]:
                if str(curr_min)[len(str_x):] != "9" * (len(str_curr_min) - len(str_x)):
                    count += (len(str_curr_min) - len(str_x))
                    x = curr_min+1
                    break

            count += 1
            x = 10*x
        curr_min = x

    return count


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        integers = [int(x) for x in input().split(" ")]
        assert len(integers) == N
        res = solve(N, integers)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)