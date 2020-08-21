'''
https://py.checkio.org/en/mission/similar-triangles/

This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Input:

Two lists as coordinates of vertices of each triangle.
Coordinates is three tuples of two integers.
Output: True or False.

Precondition:
-10 ≤ x(, y) coordinate ≤ 10
'''


from typing import List, Tuple
from itertools import starmap
from sympy import Polygon, Point, are_similar
Coords = List[Tuple[int, int]]

# I've found ppl using Simpy library to do this geometry calculus
# I need to go further and study this resource!


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    return are_similar(Polygon(*starmap(Point, coords_1)),
                       Polygon(*starmap(Point, coords_2)))


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)],
                            [(3, 0), (4, 2), (5, 0)]))
    print(similar_triangles([(0, 0), (1, 2), (2, 0)],
                            [(3, 0), (4, 3), (5, 0)]))
    print(similar_triangles([(0, 0), (1, 2), (2, 0)],
                            [(2, 0), (4, 4), (6, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)],
                             [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)],
                             [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)],
                             [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)],
                             [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)],
                             [(3, 0), (5, 4), (5, 0)]) is True, 'scal. reflect'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)],
                             [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
