from utils import arrs


def test_get():
    assert arrs.get(array:[1, 2, 3], index: 1, default: "test") == 2
    assert arrs.get(array:[], index:0, default: "test") == "test"


def test_slice():
    assert arrs.my_slice(coll:[1, 2, 3, 4], start: 1, end: 3) == [2, 3]
    assert arrs.my_slice(coll:[1, 2, 3], start: 1) == [2, 3]
