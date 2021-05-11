def backtrack(n, lastnum, templist, tempsum, k, answer):
    if len(templist) == k:
        if tempsum == n:
            answer.append(templist)
    for num in range(lastnum + 1, 10):
        if num <= n - tempsum:
            backtrack(n, num, templist + [num], tempsum + num, k, answer)
        else:
            return
    return answer
def combination(n, k):
    answer = []
    backtrack(n, 0, [], 0, k, answer)
    return answer