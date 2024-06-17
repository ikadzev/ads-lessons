def top_sort(dep: list[list[int]], dep_count: list[int]) -> list:
    sortd = []
    zero_dep = [i for i in range(len(dep_count)) if dep_count[i] == 0]
    print('z', zero_dep)

    while zero_dep:
        item = zero_dep.pop(0)
        sortd.append(item)
        for i in dep[item]:
            dep_count[i] -= 1
            if dep_count[i] == 0:
                zero_dep.append(i)

    print('s', sortd)
    return sortd if len(sortd) == len(dep_count) else None


def sortt(n: int, m: int, group: list[int], before: list[list[int]]) -> list[int]:
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1

    item_dep = [[] for _ in range(n)]
    group_dep = [[] for _ in range(m)]
    item_dep_count = [0 for _ in range(n)]
    group_dep_count = [0 for _ in range(m)]

    for i in range(n):
        for bef in before[i]:
            item_dep[bef].append(i)
            item_dep_count[i] += 1
            if group[i] != group[bef]:
                group_dep[group[bef]].append(group[i])
                group_dep_count[group[i]] += 1

    item_place = top_sort(item_dep, item_dep_count)
    if not item_place:
        return [1]

    group_place = top_sort(group_dep, group_dep_count)
    if not group_place:
        return [2]

    placed = [[] for _ in range(m)]
    for i in item_place:
        placed[group[i]].append(i)

    out = []
    for i in group_place:
        out.extend(placed[i])

    return out


n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
print(sortt(n, m, group, beforeItems))


