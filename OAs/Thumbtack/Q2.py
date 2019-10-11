from collections import defaultdict


def Q2(categories, projects, k):
    cateMap = defaultdict(list)
    recorded = set()
    for category in categories:
        c1, c2, relevance = category.split(',')
        if c1 not in recorded:
            cateMap[c1].append([c1, 1.0])
            recorded.add(c1)
        if c2 not in recorded:
            cateMap[c2].append([c2, 1.0])
            recorded.add(c2)
        cateMap[c1].append([c2, float(relevance)])
        cateMap[c2].append([c1, float(relevance)])

    res, recordedCate = [], {}
    for project in projects:
        order = []
        if project not in cateMap:
            cateMap[project].append([project, 1.0])
        for category, relevance in cateMap[project]:
            if category not in recordedCate:
                recordedCate[category] = relevance
            else:
                if relevance > recordedCate[category]:
                    recordedCate[category] = relevance

        for c, _ in sorted(recordedCate.items(), key=lambda x: (-x[1], x[0]))[:k]:
            order.append(c)
        res.append(order)
    return res


print(Q2(["House Painting,Interior Painting,0.9",
    "Handyman,Massage Therapy,0.1",
    "Handyman,House Painting,0.5",
    "House Painting,House Cleaning,0.6",
    "Furniture Assembly,Handyman,0.8",
    "Furniture Assembly,Massage Therapy,0.1",
    "Plumbing Drain Repair,Junk Removal,0.3"],
    ["House Painting", "Handyman"], 4
))

print(Q2([], ["House Painting", "Handyman"], 4))

print(Q2([], [], 4))

print(Q2(["House Painting,Interior Painting,0.9",
    "Handyman,Massage Therapy,0.1",
    "Handyman,House Painting,0.5",
    "House Painting,House Cleaning,0.6",
    "Furniture Assembly,Handyman,0.8",
    "Furniture Assembly,Massage Therapy,0.1",
    "Plumbing Drain Repair,Junk Removal,0.3"],
    [], 2
))

print(Q2(["House Painting,Interior Painting,0.9",
    "Handyman,Massage Therapy,0.1",
    "Handyman,House Painting,0.5",
    "House Painting,House Cleaning,0.6",
    "Furniture Assembly,Handyman,0.8",
    "Furniture Assembly,Massage Therapy,0.1",
    "Plumbing Drain Repair,Junk Removal,0.3"],
    ["House Painting", "Handyman"], 0
))

# duplicate projects
print(Q2(["House Painting,Interior Painting,0.9",
    "Handyman,Massage Therapy,0.1",
    "Handyman,House Painting,0.5",
    "House Painting,House Cleaning,0.6",
    "Furniture Assembly,Handyman,0.8",
    "Furniture Assembly,Massage Therapy,0.1",
    "Plumbing Drain Repair,Junk Removal,0.3"],
    ["House Painting", "Handyman", "House Painting"], 6
))

