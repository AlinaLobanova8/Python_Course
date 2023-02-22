from math import pi


def find_farthest_orbit(nums_list):
    s_dict = {pi * val[0] * val[1]: val for i, val in enumerate(nums_list) if val[0] != val[1]}
    return max(s_dict.items())[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))