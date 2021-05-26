def solve(N, formulas):
    formulas = eval_around_hashtag(formulas)

    grps = find_hashtag_grp(formulas)
    import random
    random_dict = {}
    for g in set(grps):
        random_dict[g]= [random.randint(0,1000) for _ in range(5)]
    res = []
    for i,f in enumerate(formulas):
        f_res = []
        grp = grps[i]
        for r in random_dict[grp]:
            if len(grp)> 0:
                f_res.append(eval(f.replace(grp, str(r))))
            else:
                f_res.append(eval(f))
        res.append(f_res)

    sol=[]
    class_res = []
    for i,f in enumerate(formulas):
        found = False
        for j,fres in enumerate(class_res):
            if res[i] == fres:
                sol.append(str(j+1))
                found = True
                break
        if not found:
            class_res.append(res[i])
            sol.append(str(len(class_res)))

    return sol


def eval_around_hashtag(formulas):
    new_formulas = []
    for f in formulas:
        if '#' not in f:
            f = str(eval(f))
            new_formulas.append(f)
            continue
        unknown_index = f.index("#")
        levels = [0] * len(f)
        cur_lev = 0
        for i, x in enumerate(f):
            if x == "(":
                cur_lev += 1
            if x == ")":
                cur_lev -= 1
            levels[i] = cur_lev
        # print(levels)
        eval_str_first = ""
        if unknown_index > 0:
            if f[unknown_index - 1] == ")":
                for i in range(2, len(f)):
                    if levels[unknown_index - i] == levels[unknown_index - 1]:
                        start_eval = unknown_index - i + 1
                        break
                eval_str_first = f[start_eval:unknown_index]

        if unknown_index < len(f) - 1:
            if f[unknown_index + 1] == "(":
                for i in range(2, len(f)):
                    if levels[unknown_index + i] == levels[
                        unknown_index + 1] - 1:
                        end_eval = unknown_index + i + 1
                        break
                eval_str_second = f[unknown_index + 1:end_eval]
                f = f[:unknown_index+1] + str(eval(eval_str_second)) + f[end_eval:]
        if len(eval_str_first) > 0:
            f = f[:start_eval] + str(eval(eval_str_first)) + f[unknown_index:]
        new_formulas.append(f)
    return new_formulas


def find_hashtag_grp(fs):
    grps = []
    for f in fs:
        if "#" not in f:
            grp = ""
        else:
            i = f.index("#")
            for j in range(len(f)):
                if f[i+j] == ")":
                    end = i+j+1
                    break

            for j in range(len(f)):
                if f[i-j] == "(":
                    start = i-j
                    break

            grp = f[start:end]
        grps.append(grp)
    return grps

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        formulas = []
        for i in range(N):
            formulas.append(input())
        res = solve(N, formulas)
        print("Case #{t}: {res}".format(t=t, res=" ".join(res)), flush=True)