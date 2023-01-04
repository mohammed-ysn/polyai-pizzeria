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

        # iterate through all reachable blocks from the pizzeria
        for dy in range(-r, r + 1):
            for dx in range(-r + abs(dy), r - abs(dy) + 1):
                # check if block is within the city
                if 0 <= y + dy < n and 0 <= x + dx < n:
                    city[y + dy][x + dx] += 1

        if debug:
            print(city)

    print(np.max(city))


if __name__ == "__main__":
    # main(debug=True)
    main()
