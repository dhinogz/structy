def pair_product(numbers, target_product):

    prev_map = {}

    for i, num in enumerate(numbers):
        diff = target_product / num
        if diff in prev_map:
            return (i, prev_map[diff])
        prev_map[num] = i
    return