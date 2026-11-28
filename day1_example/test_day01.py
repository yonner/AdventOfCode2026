import pytest

from day01 import main, parse_rotation, rotate, solve_1, solve_2

EXAMPLE = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


# --- parse_rotation ---------------------------------------------------------

@pytest.mark.parametrize(
    "line, expected",
    [
        ("L68", ("L", 68)),
        ("R5", ("R", 5)),
        ("R0", ("R", 0)),
        ("L1000", ("L", 1000)),
        ("R48\n", ("R", 48)),
        ("  L3  ", ("L", 3)),
    ],
)
def test_parse_rotation(line, expected):
    assert parse_rotation(line) == expected


@pytest.mark.parametrize("line", ["X10", "L", "Rabc"])
def test_parse_rotation_rejects_bad_lines(line):
    with pytest.raises(ValueError):
        parse_rotation(line)


# --- rotate ------------------------------------------------------------------

@pytest.mark.parametrize(
    "position, direction, amount, expected",
    [
        (50, "R", 10, 60),
        (50, "L", 10, 40),
        (99, "R", 1, 0),     # wraps past 99
        (0, "L", 1, 99),     # wraps below 0
        (50, "R", 50, 0),
        (50, "L", 50, 0),
        (50, "R", 100, 50),  # a full turn ends where it started
        (50, "L", 250, 0),   # several full turns
        (10, "R", 0, 10),
    ],
)
def test_rotate(position, direction, amount, expected):
    assert rotate(position, direction, amount) == expected


# --- solve_1 -----------------------------------------------------------------

def test_solve_1_puzzle_example():
    assert solve_1(EXAMPLE) == 3


def test_solve_1_empty_input():
    assert solve_1([]) == 0


def test_solve_1_counts_each_landing_on_zero():
    assert solve_1(["R50", "R100", "L100"]) == 3


def test_solve_1_passing_zero_does_not_count():
    assert solve_1(["R60"]) == 0  # goes 50 -> 10, crossing 0 on the way


def test_solve_1_handles_amounts_over_100():
    assert solve_1(["R1050", "L999", "R999"]) == 2  # 0, 1, 0


def test_solve_1_skips_blank_lines():
    assert solve_1(["R50\n", "\n", "", "L0\n"]) == 2


def test_solve_1_custom_start():
    assert solve_1(["L5"], start=5) == 1


def test_solve_2_placeholder():
    assert solve_2(EXAMPLE) == 0


# --- main --------------------------------------------------------------------

def test_main_reads_file(tmp_path, capsys):
    puzzle_input = tmp_path / "input.txt"
    puzzle_input.write_text("\n".join(EXAMPLE) + "\n", encoding="utf-8")
    main(puzzle_input)
    assert "Part 1 Answer: 3" in capsys.readouterr().out
