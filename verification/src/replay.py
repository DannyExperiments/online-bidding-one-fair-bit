"""Exact finite examples for uniform-seed online bidding."""

from fractions import Fraction


def charged(bids, target):
    total = Fraction(0)
    for bid in bids:
        total += bid
        if bid >= target:
            return total
    raise ValueError("The test schedule ends below the target.")


def round_robin(bids, seeds):
    return [bids[i::seeds] for i in range(seeds)]


def geometric_checks():
    intervals = 0
    endpoints = 0
    right_limits = 0
    for seeds in range(1, 9):
        base = 1 + Fraction(1, seeds)
        merged = [base**i for i in range(80)]
        schedules = round_robin(merged, seeds)
        optimum = base**(seeds + 1)
        assert sum(charged(seq, 1) for seq in schedules) / seeds == base**seeds - 1
        for j in range(60):
            target = (3 * merged[j] + merged[j+1]) / 4
            amount = sum(charged(seq, target) for seq in schedules)
            assert amount == sum(merged[:j+seeds+1])
            assert amount / (seeds * target) < optimum
            intervals += 1

            endpoint = merged[j]
            at_end = sum(charged(seq, endpoint) for seq in schedules)
            assert at_end == sum(merged[:j+seeds])
            assert at_end / (seeds * endpoint) < amount / (seeds * endpoint)
            endpoints += 1

            assert amount / (seeds * endpoint) == optimum - 1 / endpoint
            right_limits += 1
    print(f"Geometric schedules: {intervals} interiors, {endpoints} endpoints, {right_limits} right limits.")
    print("Initial target u=1 checked for one through eight seeds.")


def reassignment_checks():
    pools = [
        [[1, 3, 6, 40], [2, 3, 20, 40]],
        [[1, 4, 9, 40], [1, 2, 9, 40], [1, 2, 9, 40]],
        [[2, 7, 20, 51], [1, 6, 23, 51], [3, 6, 25, 51], [7, 9, 20, 51]],
    ]
    comparisons = 0
    for original in pools:
        k = len(original)
        merged = sorted(bid for seq in original for bid in seq)
        cyclic = round_robin(merged, k)
        candidates = sorted(set(merged))
        midpoints = [Fraction(x+y, 2) for x, y in zip(candidates, candidates[1:])]
        for target in [1, *candidates, *midpoints]:
            j = sum(bid < target for bid in merged)
            original_total = sum(charged(seq, target) for seq in original)
            cyclic_total = sum(charged(seq, target) for seq in cyclic)
            assert cyclic_total == sum(merged[:j+k]) <= original_total
            comparisons += 1

        epsilon = Fraction(1, 10)
        strict = [b * (1 + epsilon * (1 - Fraction(1, 2)**j))
                  for j, b in enumerate(merged, start=1)]
        assert all(x < y for x, y in zip(strict, strict[1:]))
        for j in range(len(merged) - k):
            assert sum(strict[:j+k+1]) / strict[j] <= (1 + epsilon) * sum(merged[:j+k+1]) / merged[j]
    print(f"Cyclic reassignment: {comparisons} targets in three tied test collections.")


def worked_example():
    base = Fraction(3, 2)
    bids = [base**i for i in range(9)]
    schedules = round_robin(bids, 2)
    endpoint = bids[5]
    target = (endpoint + bids[6]) / 2
    charged_above = [charged(seq, target) for seq in schedules]
    assert charged_above == [sum(bids[:7:2]), sum(bids[1:8:2])]
    assert sum(charged_above) / (2 * endpoint) == Fraction(6305, 1944)
    assert base**3 == Fraction(27, 8)
    print("Fair bit at a^5+: seed stops a^6 and a^7; right-limit ratio 6305/1944; optimum 27/8.")


if __name__ == "__main__":
    geometric_checks()
    reassignment_checks()
    worked_example()
