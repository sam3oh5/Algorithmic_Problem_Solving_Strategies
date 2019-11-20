def get_max_fence(fences):
    max_fence_length = [0] * len(fences)
    max_size = 0
    for i, f1 in enumerate(fences):
        start = i
        if i > 0 and f1 == fences[i - 1]:
            max_fence_length[i] = max_fence_length[i - 1]
            continue
        elif i > 0 and f1 < fences[i - 1]:
            start = max_fence_length[i - 1]
        for j, f2 in enumerate(fences[start + 1:], start + 1):
            if f1 > f2 or j == len(fences) - 1:
                max_fence_length[i] = j - 1
                max_size = max(max_size, f1 * (j - i))
                break
    return max_size


test = [[7, 1, 5, 9, 6, 7, 3], [1, 4, 4, 4, 4, 1, 1], [1, 8, 2, 2]]
for t in test:
    print(get_max_fence(t))
