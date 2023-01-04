import itertools
import numpy as np


def main(debug=False):
    if debug:
        import sys
        sys.stdin = open("input.txt", "r")

    n, m = (int(x) for x in input().split())
    assert 1 <= n <= 10000
    assert 1 <= m <= 10000

    city = np.zeros(shape=(n, n), dtype=int)

    for pizzeria in range(m):
        x, y, r = (int(x) for x in input().split())
        assert 1 <= x <= n
        assert 1 <= y <= n
        assert 1 <= r <= 5000

        # convert 1-based indexing to 0-based
        x -= 1
        y -= 1

        pizzeria_reach = np.zeros(shape=(n, n), dtype=int)

        for y_offset in range(r + 1):
            for x_offset in range(r + 1):
                if x_offset + y_offset > r:
                    # exceeded max dist
                    continue

                # generate all block coordinates with the current x and y
                # offsets in positive and negative directions
                reachable_blocks = itertools.product(
                    [y + y_offset, y - y_offset], [x + x_offset, x - x_offset]
                )

                for block_y, block_x in reachable_blocks:
                    if 0 <= block_x < n and 0 <= block_y < n:
                        pizzeria_reach[block_y][block_x] = 1

        city += pizzeria_reach

    print(np.max(city))


if __name__ == "__main__":
    main(debug=True)
