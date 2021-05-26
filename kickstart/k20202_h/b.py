def get_nr_first_dig(r):
    return int(r[0]) // 2


def check_even(one_dig):
    return (int(one_dig) + 1) // 2


def get_highest_digit_case(digits):
    tot = 0
    for idx, d in enumerate(digits):
        if idx % 2 == 1:
            tot += check_even(d) * 5 ** (len(digits)-(idx+1))
        else:
            tot += get_nr_first_dig(d) * 5 ** (len(digits)-(idx+1))

        if int(d) % 2 == idx % 2:
            return tot
    return tot+1


def solve_andre(r):
    # total_boring = get_nr_first_dig(r) * 5 ** (len(str(r)) - 1)
    total_boring = sum([5**x for x in range(1, len(r))])
    return total_boring + get_highest_digit_case(r)

def check_stupid(l, r):
    lint = int(l)
    rint = int(r)
    tot = 0
    for i in range(lint, rint+1):
        tot += check_boring(i)
    return tot

def check_boring(i):
    nr = str(i)
    for index,j in enumerate(nr):
        if index % 2 == 0:
            if int(j) not in [1,3,5,7,9]:
                return 0
        else:
            if int(j) not in [0,2,4,6,8]:
                return 0
    return 1

def main():
    T = int(input())
    for t in range(1, T+1):
        l, r = [x for x in input().split(" ")]
        res = solve_andre(r)
        res = res - solve_andre(str(max(int(l)-1, 0)))
        # print("should be")
        # print(check_stupid(l, r))
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()

# print(check_stupid(0,5432))