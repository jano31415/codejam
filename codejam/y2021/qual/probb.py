def solve(X,Y,art):
    if X>= 0 and Y>= 0:
        return solve_pos(X,Y,art)
    else:
        return solve_neg(X,Y,art)

def solve_pos(X,Y,art):
    current_to_xy = {"J":Y, "C":X}
    if "J" not in art:
        return 0
    if "C" not in art:
        return 0
    current = art[0]
    tot = 0
    for s in art:
        if s == "?":
            continue
        if s == current:
            continue
        else:
            if current == "?":
                current = s
            else:
                tot += current_to_xy[current]
                current = s
    return tot

def solve_neg(X,Y,art):
    if len(art) == 1:
        return 0
    representation = represent(X, Y, art)
    # CJ costs X, JC costs Y
    current_to_xy = {"J": Y, "C": X}
    swap_dict = {"J":"C", "C":"J"}
    tot = 0
    before = None
    for char, count, next in representation:
        if char != "?":
            if next != "?":
                tot += current_to_xy[char]
            before = char
        else:
            if before is None:
                tot += get_before_none(X, Y, count, current_to_xy, next,
                                      swap_dict)
            elif next is None:
                tot += get_before_none(X, Y, count, current_to_xy, swap_dict[before],
                                      swap_dict)
            else:
                if before == next:
                    if X + Y < 0:
                        tot += (X + Y) * ((count+1) // 2)
                else:
                    tot += current_to_xy[before]
                    if X + Y < 0:
                        tot += (X + Y) * (count // 2)

    # print(count_art(current_to_xy, "JCJJCJJCJC"))
    return tot

def count_art(current_to_xy, art):
    current = art[0]
    tot = 0
    for s in art[1:]:
        if s == current:
            continue
        else:
            tot += current_to_xy[current]
            current = s
    print(tot)
    return tot



def get_before_none(X, Y, count, current_to_xy, next, swap_dict):

    # since before is None, just do same as after no costs
    tot1 = 0
    tot2 = (X + Y) * (count // 2)
    if count % 2 == 1:
        tot2 += min(current_to_xy[swap_dict[next]], 0)
    tot3 = current_to_xy[swap_dict[next]]

    return min(tot1, tot2, tot3)


def represent(X,Y,art):
    representation = []
    current = art[0]
    count = 1
    for s in art[1:]:
        if s == current:
            count += 1
        else:
            representation.append((current, count, s))
            current = s
            count = 1
    representation.append((current, count, None))
    return representation

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        X,Y,art = [x for x in input().split(" ")]
        res = solve(int(X), int(Y), art)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)