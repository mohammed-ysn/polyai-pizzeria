import itertools
import numpy as np

# debugging
import sys
sys.stdin = open("input.txt", "r")

N, M = (int(x) for x in input().split())
assert 1 <= N <= 10000
assert 1 <= M <= 10000

city = np.zeros(shape=(N, N), dtype=int)

for pizzeria in range(M):
    X, Y, R = (int(x) for x in input().split())
    assert 1 <= X <= N
    assert 1 <= Y <= N
    assert 1 <= R <= 5000

    # convert 1-based indexing to 0-based
    X -= 1
    Y -= 1

    pizzeria_reach = np.zeros(shape=(N, N), dtype=int)

    for y_offset in range(R + 1):
        for x_offset in range(R + 1):
            if x_offset + y_offset > R:
                # exceeded max dist
                continue

            # generate all block coordinates with the current x and y
            # offsets in positive and negative directions
            reachable_blocks = itertools.product(
                [Y + y_offset, Y - y_offset], [X + x_offset, X - x_offset]
            )

            for block_y, block_x in reachable_blocks:
                if 0 <= block_x < N and 0 <= block_y < N:
                    pizzeria_reach[block_y][block_x] = 1

    city += pizzeria_reach

print(np.max(city))
