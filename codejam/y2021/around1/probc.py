def solve_old(N, Q, students):
    res = solve_recursive(N, Q, students, "")
    best_exam = ""
    tot_count = 0
    for i in range(Q):
        count_f = 0
        count_t = 0
        for exam in res:
            if exam[i] == "F":
                count_f += 1
            if exam[i] == "T":
                count_t += 1
        if count_f >= count_t:
            best_exam = best_exam + "F"
            tot_count += count_f
        else:
            best_exam = best_exam + "T"
            tot_count += count_t


    number_poss = len(res)
    if tot_count != 0:
        for q in reversed(range(2, number_poss+1)):
            if (tot_count % q == 0) and (number_poss%q == 0):
                tot_count = tot_count//q
                number_poss = number_poss//q

    return f"{best_exam} {tot_count}/{number_poss}"


def solve_recursive(N, Q, students, exam):

    for s,correct in students:
        count = 0
        for i, guess in enumerate(s):
            if i+1 > len(exam):
                break
            if guess == exam[i]:
                count += 1
        if count + (Q - len(exam)) < correct:
            return []
        if count > correct:
            return []
    if len(exam) == Q:
        return [exam]


    return solve_recursive(N, Q, students, exam+"F") + solve_recursive(N, Q, students, exam+"T")


def solve(N, Q, students):
    count_same= 0
    count_diff = 0
    exam1 = students[0][0]
    exam2 = students[1][0]

    for i in range(Q):
        if exam1[i] == exam2[i]:
            count_same += 1
        else:
            count_diff += 1
    correct1 = students[0][1]
    correct2 = students[1][1]
    correct_same = ((correct2+correct1) - count_diff) //2
    diff1 = correct1 - correct_same
    diff2 = correct2 - correct_same
    if correct_same > max(correct2, correct1):
        print("fail1")
    if diff2 + diff1 > count_diff:
        print("fail")
    return find_optimal_str(correct_same, count_same, diff1, diff2, count_diff, [exam1, exam2])

def find_optimal_str(correct_same, count_same, diff1, diff2, count_diff, exams):
    if (count_same-correct_same) > correct_same:
        reverse_same = True
    else:
        reverse_same = False
    max_diff = max([(count_diff-diff1), diff1, (count_diff-diff2), diff2])
    reverse_diff = False
    if (count_diff - diff1) == max_diff:
        use_student = 0
        reverse_diff = True
    if diff1 == max_diff:
        use_student = 0
        reverse_diff = False
    if (count_diff - diff2) == max_diff:
        use_student = 1
        reverse_diff = True
    if diff2 == max_diff:
        use_student = 1
        reverse_diff = False
    not_dict = {"T": "F", "F": "T"}
    new_str = ""
    diff_list = [diff1, diff2]
    same = 0
    diff = 0
    for i,guess in enumerate(exams[use_student]):
        if exams[0][i] == exams[1][i]:
            if reverse_same:
                new_str += not_dict[exams[use_student][i]]
                same = count_same - correct_same
            else:
                new_str += exams[use_student][i]
                same = correct_same
        else:
            if reverse_diff:
                new_str += not_dict[exams[use_student][i]]
                diff = count_diff - diff_list[use_student]
            else:
                new_str += exams[use_student][i]
                diff = diff_list[use_student]
    return f"{new_str} {diff+same}/1"

def dp(N, Q, students):
    ind_to_type = {} #["FFT", "FTF", "FTT", "FFF"]
    s = [x[0] for x in students]
    c = [x[1] for x in students]
    s1,c1 = students[0]
    s2,c2 = students[1]
    s3,c3 = students[2]
    not_dict = {"T": "F", "F": "T"}

    for i in range(Q):
        if s1[i] != "F":
            if i >0:
                for j,si in enumerate(s):
                    not_str = not_dict[si[i]]

                    if i != 0 :
                        si = si[:i-1]+ not_str+ si[i:]
                    else:
                        si = not_str+ si[i:]
                    s[j] = si
    for i in range(Q):
        str_type = ""
        for si in s:
            str_type += si[i]
        ind_to_type["str_type"] = ind_to_type.get(str_type, 1)
    #??



if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, Q = [int(x) for x in input().split(" ")]
        students = []
        for i in range(N):
            guess, correct = [x for x in input().split(" ")]
            students.append((guess,int(correct)))
            assert len(guess) == Q
        assert len(students) == N
        import time
        a = time.time()
        if N == 2:
            # res1 = solve_old(N, Q, students)
            res = solve(N, Q, students)
            # print(res1)
            # print(res)
        if N == 1:
            not_dict = {"T": "F", "F": "T"}
            guess,correct = students[0]
            rev_guess = ""
            if correct <= Q//2:
                for x in guess:
                    rev_guess += not_dict[x]
                guess = rev_guess
                correct = Q - correct
            f"{guess} {correct}/1"
            res = solve_old(N, Q, students)
        if N == 3:
            res = dp(N,Q,students)
        b = time.time()
        # print(b-a)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)