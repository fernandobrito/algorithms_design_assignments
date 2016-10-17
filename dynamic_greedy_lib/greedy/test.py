def comp(x, y):
    return x[0] / x[1] > y[0] / y[1]

items = [[60, 10], [100, 20], [120, 30]]

sorted_items = sorted(items, key=lambda item: item[0] / item[1])

sorted_items = sorted_items[::-1]

print(sorted_items)


'''
for edge in graph:
    if not edge[1] in v:
        v.append(edge[1])

    if not edge[2] in v:
        v.append(edge[2])

print(v)
'''