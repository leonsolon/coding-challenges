def solution(A):
    # write your code in Python 3.6
    min_values = []
    max_values = []

    if min(A) * max(A) > 0:
        product = 1
        for i in range(0, 3):
            max_A = max(A)
            index_max = A.index(max_A)
            product *= A.pop(index_max)
    else:
        for i in range(0,3):
            if len(A) > 0:
                max_A = max(A)
                if max_A >= 0:
                    index_max = A.index(max_A)
                    max_values.append(A.pop(index_max))
            if len(A) >0:
                min_A = min(A)
                if min_A < 0:
                    index_min = A.index(min_A)
                    min_values.append(A.pop(index_min))

        len_max_values = len(max_values)
        len_min_values = len(min_values)
        if len_max_values >= 3 and len_min_values >= 2:
            product_max = max_values[0] * max_values[1] * max_values[2]
            product_min = min_values[0] * min_values[1] * max_values[0]
            product = max(product_min, product_max)
        elif len_max_values >= 3:
            product = max_values[0] * max_values[1] * max_values[2]
        elif len_min_values >= 2 and len_max_values >= 1:
            product = min_values[0] * min_values[1] * max_values[0]
    return product
