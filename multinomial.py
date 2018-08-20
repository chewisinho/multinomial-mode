import math


def multinomial_mode_from_lower(n, p_list, x_0=None):
    """Computes the mode of a multinomial distribution using Algorithm I from the paper:
    https://www.sciencedirect.com/science/article/pii/S0167715202004303

    Args:
        n (int): The number of trials of the multinomial distribution.
        p_list (list): An array containing the probability values for the categories.

    Optional:
        x_0 (float): Optionally specify a lower bound x_0 such that sum([math.floor(x_0 * p) for p in p_list]) < n.

    Returns:
        list: A mode of the multinomial distribution.
    """
    r = len(p_list)
    if x_0 is None:
        x_0 = n
    while True:
        k = [math.floor(x_0 * p) for p in p_list]
        f = [x_0 * p_list[i] - k[i] for i in range(r)]
        n_0 = sum(k)
        if n_0 < n:
            break
        x_0 /= 2
    q = [(1 - f[i]) / p_list[i] for i in range(r)]
    x = x_0
    while n_0 < n:
        a = min(list(range(r)), key=lambda i: q[i])
        k[a] += 1
        n_0 += 1
        if n_0 < n:
            q[a] += 1 / p_list[a]
        else:
            x = x_0 + q[a]
    x = x_0 + q[a]
    return [math.floor(x * p) for p in p_list]
