import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_n_more_than_or_eq_ten():
    input_arr = [5,6,3,2,1,4,0,7,8,9]
    assert Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 1
    assert Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == 1

    input_marr = [0,2,5,3,4,6,9,8,7,0,2,1,3,6,2,4,5,7,6,3,2,0,1,2,3,6]
    
    assert Lab3.bubble_sort(input_marr, Lab3.SORT_DESCENDING) == 1
    assert Lab3.bubble_sort(input_marr, Lab3.SORT_DESCENDING) == 1

def test_empty_arr():
    assert Lab3.bubble_sort([], Lab3.SORT_ASCENDING) ==0
    assert Lab3.bubble_sort([], Lab3.SORT_DESCENDING) ==0

def test_not_int():
    assert Lab3.bubble_sort(["a",1,2,3,4,5], Lab3.SORT_ASCENDING) ==2
    assert Lab3.bubble_sort(["a",1,2,3,4,5], Lab3.SORT_DESCENDING) ==2

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])