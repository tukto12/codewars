from itertools import combinations


def choose_best_sum(t, k, ls):
    comb = combinations(ls, k)
    comb = list(comb)

    for idx, item in enumerate(comb):
        comb[idx] = [x for x in item]

    sum_list = []
    for i in comb:
        sum_list.append(sum(i))

    sum_list.sort(reverse=True)

    for item in sum_list:
        if item <= t:
            return item

    return None
