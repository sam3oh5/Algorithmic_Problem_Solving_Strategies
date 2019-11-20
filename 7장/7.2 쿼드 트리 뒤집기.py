def get_updown_reverse(quad_tree_sentence):
    quad_tree_sentence = quad_tree_sentence[1:]
    quad_list = ['x']
    while quad_tree_sentence:
        if quad_tree_sentence[0] != 'x':
            quad_list.append(quad_tree_sentence[0])
            quad_tree_sentence = quad_tree_sentence[1:]
        else:
            quad_sentence, quad_tree_sentence = get_updown_reverse(quad_tree_sentence)
            quad_list.append(quad_sentence)
        if len(quad_list) == 5:
            return ''.join(['x'] + quad_list[3:]+quad_list[1:3]), quad_tree_sentence
    return ''.join(['x'] + quad_list[3:]+quad_list[1:3]), quad_tree_sentence


def reverse(quad_tree_sentence, start=0) -> (str, int):
    head = quad_tree_sentence[start]
    start += 1
    if head != 'x':
        return head, start
    upper_left, start = reverse(quad_tree_sentence, start)
    upper_right, start = reverse(quad_tree_sentence, start)
    lower_left, start = reverse(quad_tree_sentence, start)
    lower_right, start = reverse(quad_tree_sentence, start)
    return 'x' + lower_left + lower_right + upper_left + upper_right, start


test = ['xbwwb', 'xbwxwbbwb', 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb']
for t in test:
    print(get_updown_reverse(t)[0])
    print(reverse(t)[0])