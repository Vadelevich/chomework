from chomework.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([],2) == -1
    assert index_of([1, 2, 3, 4, 5], 5, -3) == 4
    assert index_of([1, 2, 3, 4, 5],7) == -1 
