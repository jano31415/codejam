def solve(s):
    n=len(s)
    mid = n//2
    if s[mid] == s[mid+1]:
        return "Draw"
    if s[mid:] == s[:mid][::-1]:
        return "Draw"
    else:
        return "Alice"
    # for i in range(mid):



    #
    # left=-1
    # right=n
    # # greedy one look ahead
    # for i in range(n):
    #     if left+1 >= right:
    #         return "Draw"
    #     left_next = left+1
    #     right_next = right-1
    #     if s[left_next] < s[right_next]:
    #         # take left because else b takes left and loss
    #         left = left_next
    #         alice = s[left_next]
    #     elif s[left_next] > s[right_next]:
    #         right = right_next
    #         alice = s[right_next]
    #     else:
    #         # same
    #         left_next2 = left_next+1
    #         right_next2 = right_next-1
    #
    #         if s[left_next2] < s[right_next2]:
    #             right=right_next
    #             alice=s[right_next]
    #         else:
    #             left=left_next
    #             alice=s[left_next]
    #     left_next = left+1
    #     right_next = right-1
    #     if min(s[left_next], s[right_next]) < alice:
    #         return "Bob"
    #     elif min(s[left_next], s[right_next]) > alice:
    #         return "Alice"
    #     else:
    #         if s[left_next] < s[right_next]:
    #             left = left_next
    #         # else:
    #         elif s[left_next] > s[right_next]:
    #             right=right_next
    #         else:
    #             if left_next == right_next:
    #                 right = right_next
    #             else:
    #                 left_next2 = left_next + 1
    #                 right_next2 = right_next - 1
    #                 if s[left_next2] < s[right_next2]:
    #                     right = right_next
    #                 else:
    #                     left = left_next
    # return "Draw"

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        s = input().decode().strip()
        res=solve(s)
        print(res)

