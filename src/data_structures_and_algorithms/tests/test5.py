def permutation(l, k):
    def backtracking(idx, expr, countA):
        if idx == k:
            s = "".join(expr)
            res.append(s)
        else:
            for ch in l:
                if ch == "A":
                    countA += 1
                if not ((ch == "L" and expr[-2:] == ["L", "L"]) or countA == 2):
                    expr.append(ch)
                    backtracking(idx + 1, expr, countA)
                    expr.pop()
                if ch == "A":
                    countA -= 1

    res = []
    backtracking(0, [], 0)
    return res, len(res)


if __name__ == '__main__':
    l = ["A", "P", "L"]
    k = 4
    print(permutation(l, k))
