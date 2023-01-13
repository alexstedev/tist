""" Priority Tests

Test conversions between Todoist and Taskwarrior priorities.
"""
import pytest

from tist import utils


def test_ti_priority_to_tw():
    assert utils.ti_priority_to_tw(1) == None
    assert utils.ti_priority_to_tw(2) == "L"
    assert utils.ti_priority_to_tw(3) == "M"
    assert utils.ti_priority_to_tw(4) == "H"


def test_tw_priority_to_ti():
    assert utils.tw_priority_to_ti(None) == 1
    assert utils.tw_priority_to_ti("L") == 2
    assert utils.tw_priority_to_ti("M") == 3
    assert utils.tw_priority_to_ti("H") == 4
