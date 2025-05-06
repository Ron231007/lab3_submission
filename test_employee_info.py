import employee_info

def test_calculate_average_salery():
    assert int(employee_info.calculate_average_salary()) == 60166


def test_get_employees_by_age_range():
    assert employee_info.get_employees_by_age_range(23,40) == [employee_info.employee_data[0],employee_info.employee_data[1],employee_info.employee_data[3],employee_info.employee_data[4]]


def test_get_employees_by_dept():
    assert employee_info.get_employees_by_dept("Sales") == [employee_info.employee_data[0],employee_info.employee_data[5]]
    assert employee_info.get_employees_by_dept("Marketing") == [employee_info.employee_data[1],employee_info.employee_data[2]]
    assert employee_info.get_employees_by_dept("Engineering") == [employee_info.employee_data[3],employee_info.employee_data[4]]