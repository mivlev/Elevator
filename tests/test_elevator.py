import pytest
from src.Elevator import calc_floor_order
from src.Elevator import calc_travel_time


def test_calc_floor_order() -> None:

    assert calc_floor_order(True, 2, [2, 3]) == [2, 3]

    assert calc_floor_order(False, 2, [2, 3]) == [2, 3]

    assert (calc_floor_order(True, 10, [6, 8, 10, 12, 18, 22, 34]) ==
            [10, 8, 6, 12, 18, 22, 34])

    assert (calc_floor_order(False, 10, [2, 3, 4, 6, 8, 10, 15, 16]) ==
            [10, 15, 16, 8, 6, 4, 3, 2])

    assert calc_floor_order(True, 2, [-3, 0, 2, 10]) == [2, 0, -3, 10]


def test_calc_travel_time() -> None:
    assert calc_travel_time([2, 3]) == 10

    assert calc_travel_time([10, 8, 6, 12, 18, 22, 34]) == 320

    assert calc_travel_time([10, 15, 16, 8, 6, 4, 3, 2]) == 200

    assert calc_travel_time([2, 0, -3, 10]) == 180
