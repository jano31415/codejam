def solve(dna):
    # print(dna)
    counts = [(dna.count(x),x) for x in "ANTO"]
    counts.sort()
    max_tot = -1
    res = ""
    for grpa in ["AT", "AN", "AO", "NT", "NO", "TO"]:
        grpa = list(grpa)
        grpb = [x for x in "ANTO" if x not in grpa]
        dna2 = dna.replace(grpa[0], grpa[1])
        dna2 = dna2.replace(grpb[0], grpb[1])
        grpa_count = dna.count(grpa[0]) + dna.count(grpa[1])
        grpb_count = dna.count(grpb[0]) + dna.count(grpb[1])
        dna3,tot = get_worst_case(grpa_count, grpb_count, dna2, grpa[1], grpb[1])
        dna_a = "".join([x for x in dna if x in grpa])
        dna_b = "".join([x for x in dna if x in grpb])
        was_swaped = False
        if len(dna3) == 0:
            # print(grpb)
            get_worst_case(grpa_count, grpb_count, dna2, grpa[1], grpb[1])
        if dna3[0] == grpb[1]:
            print("swap")
            print(dna3)
            swap = dna_a
            dna_a = dna_b
            dna_b = swap
            swap = grpa
            grpa = grpb
            grpb = swap
            # was_swaped =True


        dna_left,tot1 = get_worst_case(dna_a.count(grpa[0]), dna_a.count(grpa[1]), dna_a, grpa[0],grpa[1])
        dna_right,tot2 = get_worst_case(dna_b.count(grpb[0]), dna_b.count(grpb[1]), dna_b, grpb[0], grpb[1])
        if max_tot < tot+tot1+tot2:
            max_tot = tot+tot1+tot2
            res = dna_left+dna_right
            # if was_swaped:
            #     res = dna_right+dna_left
    print(max_tot)
    return res


def get_worst_case(grpa_count,grpb_count, dna2, a, b):
    tot = left_right_count(dna2, a, 0, grpa_count)
    tot2 = left_right_count(dna2, a, grpb_count, 0)
    # print(dna2)
    # print(tot)
    # print(tot2)
    dna2 = (a * grpa_count) + (b * grpb_count)
    if tot < tot2:
        dna2 = dna2[::-1]
    return dna2, max(tot,tot2)


def left_right_count(dna2, a, grpa_assigned, grpb_assigned):
    tot = 0
    for i, d in enumerate(dna2):
        if d == a:
            tot += abs(i - grpa_assigned)
            grpa_assigned += 1
        else:
            tot += abs(i - grpb_assigned)
            grpb_assigned += 1
    return tot//2


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        dna = input()
        res = solve(dna)
        print("{res}".format(res=res), flush=True)