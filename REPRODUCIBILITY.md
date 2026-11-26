# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay checks 480 geometric intervals, their inclusive endpoints and their right limits. It also checks the initial target for one through eight seeds, cyclic reassignment and its tie perturbation on three small schedules, and the worked fair-bit example. [Recorded replay](verification/results/replay.txt).

Open index.html from the [offline explorer archive](visualization/interleaved-bids-explorer.zip) to choose a breakpoint and see the costs. [Build the paper](paper/BUILD.md).
