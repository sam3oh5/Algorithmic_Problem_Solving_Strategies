def solution_by_myself_1(boxes, k):
    premain = [boxes[0] % k]
    psum = {0: 1}
    value = boxes[0] % k
    if value in psum:
        psum[value] += 1
    else:
        psum[value] = 1
    for idx, box in enumerate(boxes[1:], 1):
        value = (premain[idx - 1] + box) % k
        premain.append(value)
        if value in psum:
            psum[value] += 1
        else:
            psum[value] = 1
    return sum([v * (v - 1) for v in psum.values()]) // 2


boxes = [1, 2, 3, 4, 5, 6]
k = 4
print(solution_by_myself_1(boxes, k))


def solution_by_myself_2(boxes, k):
    if len(boxes) == 0:
        return 0
    premain = [0, boxes[0] % k]
    for idx, box in enumerate(boxes[1:], 1):
        value = (premain[idx] + box) % k
        premain.append(value)
    length = len(premain) - 2
    while length >= 0:
        if premain[-1] == premain[length]:
            break
        length -= 1
    if length < 0:
        if premain:
            return 0
        else:
            return 1
    else:
        return max(1 + solution_by_myself_2(boxes[:length], k), solution_by_myself_2(boxes[:-1], k))


boxes = [1, 2, 3, 4]
k = 1
print(solution_by_myself_2(boxes, k))