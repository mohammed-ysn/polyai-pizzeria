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
        x_centre, y_centre, r = (int(x) for x in input().split())
        assert 1 <= x_centre <= n
        assert 1 <= y_centre <= n
        assert 1 <= r <= 5000

        # convert 1-based indexing to 0-based
        x_centre -= 1
        y_centre -= 1

        # iterate through the square of length 2r + 1
        # centred at the pizzeria
        for y in range(max(y_centre - r, 0), min(y_centre + r + 1, n)):
            for x in range(max(x_centre - r, 0), min(x_centre + r + 1, n)):
                if abs(x - x_centre) + abs(y - y_centre) > r:
                    continue

                city[y][x] += 1

    print(np.max(city))


if __name__ == "__main__":
    main(debug=True)
