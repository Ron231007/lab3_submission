import price_info 

def test_total_cost_shopping():
    assert price_info.total_cost_shopping() == 46.75


def test_cost_of_fruit():
    
    test_cases = {
        "apple": 12.0,
        "orange": 14.0,
        "watermelon": 65.0,
        "pineapple": 27.0,
        "pear": 9.0,
        "papaya": 29.5,
        "pomegranate": 49.5
    }

    for fruit, expected in test_cases.items():       #fruit is key and expected is value
        assert price_info.cost_of_fruits(fruit, 10) == expected
    
    
    
    # assert price_info.cost_of_fruits("apple", 10) == 12.0
    # assert price_info.cost_of_fruits("orange", 10) == 14.0
    # assert price_info.cost_of_fruits("watermelon", 10) == 65.0
    # assert price_info.cost_of_fruits("pineapple", 10) == 27.0
    # assert price_info.cost_of_fruits("pear", 10) == 9.0
    # assert price_info.cost_of_fruits("papaya", 10) == 29.5
    # assert price_info.cost_of_fruits("pomegranate", 10) == 49.5
