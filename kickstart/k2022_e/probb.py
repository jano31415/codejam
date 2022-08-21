# sounds like binary search
# they can not pick themselves
# success 12:34

def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] > find_this_number:
            right = middle
        else:
            left = middle + 1
    return right - 1

def solve(n, students):
    res=[""]*n
    mentors = students[:]
    mentors.sort()
    for i,s in enumerate(students):
        left = binary_search_leftmost(mentors, 2*s)
        mentor_rating = mentors[left]
        if mentor_rating == s:
            if left != 0:
                mentor_rating = mentors[left-1]
            else:
                mentor_rating =-1

        res[i] = str(mentor_rating)
    return " ".join(res)

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        students = [int(x) for x in input().split()]
        res = solve(n, students)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

