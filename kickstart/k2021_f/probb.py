import math
def solve(d,n,k, events):
    events.sort(key=lambda x: -x[0])
    day_arr,mid= binary_search_leftmost(d, events, k)
    max_v = 0
    max_i = 0
    day_i = [(i,day_arr[i]) for i in range(len(day_arr))]
    day_i.sort(key=lambda x: -x[1])
    day_i = [x for x in day_i if x[1]+k*events[mid][0] > day_i[0][1]]
    print(day_i)
    max_tot = 0
    for max_i,d in  day_i[:1000]:
        tot_v=0
        event_count=0
        for h,l,r in events:
            if (l <= max_i) and (r >= max_i):
                tot_v+= h
                event_count +=1
            if event_count == k:
                break
        if tot_v > max_tot:
            max_tot = tot_v


    return max_tot

def binary_search_leftmost(d, events, k):
    left = 0
    right = len(events)-1
    while left < right:
        middle = math.floor((left + right) / 2)
        go_right, res = check_smaller(events, middle, k)
        if go_right:
            left = middle + 1
        else:
            right = middle
    go_left, res = check_smaller(events, left, k)
    return res, left

def check_smaller(array, middle, find_this_number):
    # might be slightly different if this is not an array
    res1,res2 = difference_array([0]*d, events, middle)
    return max(res1) < find_this_number, res2
# max range query

def difference_array(arr2, events, middle):
    # create a difference array
    diff = arr2
    vals = arr2[:]
        # [arr2[0]] + [arr2[i] - arr2[i - 1] for i in range(1, len(arr2))]
    # update the range by adding the value for the first and then subtracting it
    # at the end of the range
    for i in range(middle+1):
        v,l,r = events[i]
        diff[l-1] += 1
        vals[l-1] += v
        if r < len(arr2):
            diff[r] -= 1
            vals[r] -= v

    # reconstruct the updated array
    for i in range(len(arr2)):
        if i == 0:
            arr2[0] = diff[0]
        else:
            arr2[i] = diff[i] + arr2[i - 1]

    for i in range(len(vals)):
        vals[i] = vals[i] + vals[i - 1]
    return arr2, vals

def solve_naiv(d,n,k,events):
    events.sort(key=lambda x: -x[0])
    max_h = 0
    for i in range(1,d+1):
        tmp=0
        count = 0
        for e in events:
            h,l,r= e
            if (i >= l) and(r >=i):
                tmp+=h
                count +=1
            if count == k:
                break
        if tmp  > max_h:
            max_h = tmp
    return max_h


# def solve2(d,n,k,events):

# over n for each day,
# find the best k  such that day is in si,ei
# will be slow for k==n, si,ei = 0,n

# sort events by h, add to each day where they

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        d,n,k = [int(x) for x in input().split(" ")]
        events = []
        for i in range(n):
            hi, si, ei = [int(x) for x in input().split(" ")]
            events.append((hi,si,ei))

        res = solve(d,n,k, events)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)


# d=30
# n=20
# k=5
# # from random import randint
# # h = [randint(1,50) for _ in range(n)]
# # l = [randint(1,d) for _ in range(n)]
# # r = [l[i] + randint(0,d-l[i]) for i in range(n)]
# # events= [(h[i], l[i], r[i]) for i in range(n)]
# # print(solve_naiv(d,n,k,events))
# # print(solve(d,n,k,events))
#
# events= [(50, 13, 28),
#  (49, 28, 30),
#  (45, 16, 21),
#  (43, 16, 29),
#  (41, 3, 10),
#  (37, 26, 30),
#  (26, 18, 20),
#  (25, 6, 30),
#  (24, 24, 29),
#  (20, 24, 24),
#  (19, 23, 27),
#  (16, 29, 30),
#  (14, 16, 16),
#  (14, 30, 30),
#  (13, 30, 30),
#  (12, 23, 29),
#  (9, 25, 25),
#  (8, 11, 15),
#  (6, 2, 24),
#  (4, 10, 22)]
#
# print(solve_naiv(d,n,k,events))
# print(solve(d,n,k,events))