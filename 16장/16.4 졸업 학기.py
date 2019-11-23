def solution(k, l, requires, classes):
    took_classes = 0
    requires = [int(sum([1 << r for r in res])) for res in requires]
    ans = 'Impossible'
    for idx, cl in enumerate(classes):
        tmp = 0
        for c in cl:
            if (took_classes & (1 << c)) == 0:
                if requires[c] == 0:
                    tmp += 1 << c
                    k -= 1
                elif (took_classes & requires[c]) == requires[c]:
                    tmp += 1 << c
                    k -= 1
        if k == 0:
            ans = idx + 1
            break
        took_classes += tmp
    return ans

k = 4
l = 4
requires = [[], [0], [0, 1, 3], []]
classes = [[0,1,2,3], [0, 1, 2, 3], [0, 1, 3], [0, 1, 2, 3]]
print(solution(k, l, requires, classes))