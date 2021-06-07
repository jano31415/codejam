def solve(bits):
    # if beautfiul than all before also
    tot = 0 # first one always beautfiul
    # print(bits)
    last = ""
    last_beautfiul_index = 0
    not1 = {"1": "0", "0": "1"}
    for i,b in enumerate(bits):
        # if i == 0:
        #     continue

        if last != "?":
            if last != b:
                if b == "?" and last in ["0","1"]:
                    last = not1[last]
                else:
                    last = b
            else:
                last_beautfiul_index=0
                for j in reversed(range(0,i)):
                    if bits[j] != "?":
                        last_beautfiul_index = j+1
                        break
                last = b
        else:
            last = b
            if b == last:
                pass
        # print(bits[last_beautfiul_index:i + 1])
        tot += (i + 1) - last_beautfiul_index
        # print(f"tot: {tot}")
    return tot

def solve_rec(bits, last="?"):
    return solve_rec(bits[:len(bits)//2]) + solve_rec(bits[:len(bits)//2])



if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        bits = input()
        res = solve(bits)
        print(str(res), flush=True)