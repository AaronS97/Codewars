def count_positives_sum_negatives(arr):
    pos_count = 0
    negatives = [] 
    if len(arr) > 0:
        for n in arr:
            if n > 0:
                pos += 1
            elif n < 0:
                negatives.append(n)
        return ([pos, sum(negatives)])
    else:
        return []