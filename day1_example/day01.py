"""Testable version of the dial puzzle solution in testExample2.py."""

from pathlib import Path

DIAL_SIZE = 100
START_POSITION = 50


def parse_rotation(line):
    """Turn a line like 'L68' into ('L', 68)."""
    line = line.strip()
    direction, amount = line[0], int(line[1:])
    if direction not in ("L", "R"):
        raise ValueError(f"Unknown direction in line: {line!r}")
    return direction, amount


def rotate(position, direction, amount):
    """Return the dial position after turning left or right by amount."""
    step = -amount if direction == "L" else amount
    return (position + step) % DIAL_SIZE


def solve_1(lines, start=START_POSITION):
    """Count how many rotations leave the dial pointing at 0."""
    position = start
    zeros = 0
    for line in lines:
        if not line.strip():
            continue
        position = rotate(position, *parse_rotation(line))
        if position == 0:
            zeros += 1
    return zeros


def solve_2(lines):
    """Part 2 is not solved yet."""
    return 0


def main(file_path):
    lines = Path(file_path).read_text(encoding="utf-8").splitlines()
    print(f"Part 1 Answer: {solve_1(lines)}")
    print(f"Part 2 Answer: {solve_2(lines)}")


if __name__ == "__main__":
    main(Path.cwd() / "input_f.txt")
