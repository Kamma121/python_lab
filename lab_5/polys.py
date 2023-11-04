def add_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    poly1 = poly1 + [0] * (max_len - len(poly1))
    poly2 = poly2 + [0] * (max_len - len(poly2))
    return [poly1[i] + poly2[i] for i in range(max_len)]


def sub_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    poly1 = poly1 + [0] * (max_len - len(poly1))
    poly2 = poly2 + [0] * (max_len - len(poly2))
    return [poly1[i] - poly2[i] for i in range(max_len)]


def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    return result


def is_zero(poly):
    return all(coef == 0 for coef in poly)


def eq_poly(poly1, poly2):
    return poly1 == poly2


def eval_poly(poly, x0):
    result = 0
    for coef in reversed(poly):
        result = result * x0 + coef
    return result


def combine_poly(poly1, poly2):
    result = []
    for coef in reversed(poly1):
        result = mul_poly(result, poly2)
        result = add_poly(result, [coef])
    result.pop()
    return result


def pow_poly(poly, n):
    result = [1]
    for _ in range(n):
        result = mul_poly(result, poly)
    return result


def diff_poly(poly):
    result = []
    for i in range(1, len(poly)):
        result.append(poly[i] * i)
    return result
