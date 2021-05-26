def solve(C):
    # print(C)
    asci_list = [ord(x) for x in C]
    # print(asci_list)
    last_min = 0
    max_str_len = 1
    curr = asci_list[0]
    max_str_list = []
    for i,x in enumerate(asci_list):
        if i == 0:
            curr = x
            continue
        if x <= curr:
            max_str_list += [j-last_min+1 for j in range(last_min, i)]
            last_min = i
        curr = x

    max_str_list += [j - last_min + 1 for j in range(last_min, i+1)]
    # print(max_str_list)
    max_str_list = [str(x) for x in max_str_list]
    return max_str_list


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        C = input()
        assert len(C) == N
        res = solve(C)
        print("Case #{t}: {res}".format(t=t, res=" ".join(res)), flush=True)