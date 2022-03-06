def solve(kingdom):
    if kingdom[-1].lower() == "y":
        return "nobody"
    if kingdom[-1].lower() in set(["o","e","i","u","a"]):
        return "Alice"
    return "Bob"



if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        kingdom = input()
        res = solve(kingdom)
        print(f"Case #{t}: {kingdom} is ruled by {res}.")