from chomework.slice import my_slice
def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert my_slice([], 1) == []
    assert my_slice([1, 2, 3, 4, 5], -4, -2) == [2, 3]
