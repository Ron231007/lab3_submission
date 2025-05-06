import lab2_submission.lab2 as lab2

def test_find_min_max():
    assert lab2.min_max_temperature([1,2,3,4,5,6,7,8,9]) == [1,9]

def test_find_ave():
    assert lab2.average_temperature([1,2,3,4,5,6,7,8,9,10]) == 5.5

def test_median_temp():
    assert lab2.calc_median_temperature([1,2,3,4,5]) == 3
