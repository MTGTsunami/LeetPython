from collections import defaultdict

d = defaultdict(list)
d["k"].append(1)
d["k"].append(2)
d["s"].append(3)
if not d["a"]:
    print("#")
    print(d["a"])
    print(d.get("a"))
else:
    print("$")


dic = {}
dic["a"] = []
dic["a"].append(1)
print(dic)