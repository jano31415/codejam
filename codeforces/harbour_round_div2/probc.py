def solve(s):
    team1 = 0
    team2 = 0
    team1_sol = 10
    for i in range(10):
        if i %2 ==0:
            if s[i] in ["?", "1"]:
                team1+=1
        else:
            if s[i] in ["1"]:
                team2 += 1

        if team1 - team2 > ((9 - i)//2 + (9-i)%2):
            team1_sol = i+1
            break

    team2_sol=10
    team1 = 0
    team2 = 0
    for i in range(10):
        if i %2 ==0:
            if s[i] in ["1"]:
                team1+=1
        else:
            if s[i] in ["?","1"]:
                team2 += 1
        if team2 - team1 > (9 - i)//2:
            team2_sol = i+1
            break
    return min(team1_sol, team2_sol)

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        s=input().decode().strip()
        res=solve(s)
        print(res)