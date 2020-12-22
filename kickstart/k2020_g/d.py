def solve_rec(cards, prob):
    if len(cards) == 2:
        return prob * (cards[0]+cards[1])
    tot = 0
    for i, c in enumerate(cards):
        if i == len(cards)-1:
            break
        new_cards = cards[:]
        new_cards[i] = new_cards[i+1] + new_cards[i]
        del new_cards[i+1]
        #print(len(new_cards))
        new_prob = prob*(1/(len(cards)-1))
        tot += new_prob * new_cards[i] + solve_rec(new_cards, new_prob)
    return tot

def solve(cards):
    n = len(cards)
    tot=0
    for j,c in enumerate(cards):
        tmp = sum([get_prob(n, i,j) for i in range(1, n)]) * c
        tot += tmp
    return tot

def get_prob(n, i,j):
    if i == 1:
        return 1
    round_nr = n-i
    if j==0 or j == n-1:
        return 1/i
    space = min(j, n-j-1)
    if round_nr>= space:
        return 1/i + 0
    return 2/i


def main():
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        cards = [int(x) for x in input().split(" ")]

        res = solve_rec(cards, 1)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()