def solution(pairs):
    if len(pairs.keys()) == 2:
        keys = list(pairs.keys())
        if keys[0] in pairs[keys[1]]:
            return 1
        else:
            return 0
    key = list(pairs.keys())[0]
    candis = pairs[key]
    del pairs[key]
    answer = 0
    for c in candis:
        if c in pairs:
            new_pairs = {key: value for key, value in pairs.items() if key != c}
            answer += solution(new_pairs)
    return answer


test3 = {
        0: [1, 2],
        1: [0, 2, 3, 4],
        2: [0, 1, 3, 4],
        3: [1, 2, 4, 5],
        4: [1, 2, 3,5 ],
        5: [3, 4]
    }
print(solution(test3))