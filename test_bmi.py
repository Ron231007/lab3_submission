import lab2_submission.bmi as bmi

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.63,42.5) == -1

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.7,65) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.7,75) == 1