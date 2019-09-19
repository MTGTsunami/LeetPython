import sys
for line in sys.stdin:
    visited, end = set(), False
    ans = ""
    for s in line:
        if s.isdigit():
            if not end:
                visited.add(s)
            else:
                if s in visited:
                    ans += s + ","
        elif s == ";":
            end = True
    print(ans[:-1])



