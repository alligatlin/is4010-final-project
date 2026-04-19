from main import calculate_stats

# Test 1: Basic addition
def test_total_calculation():
    data = [{'category': 'Ads', 'amount': '100'}, {'category': 'Ads', 'amount': '50'}]
    total, _ = calculate_stats(data)
    assert total == 150.0

# Test 2: Category grouping
def test_category_grouping():
    data = [{'category': 'Ads', 'amount': '100'}, {'category': 'PR', 'amount': '50'}]
    _, categories = calculate_stats(data)
    assert categories['Ads'] == 100.0
    assert categories['PR'] == 50.0

# Test 3: Handling empty files
def test_empty_data():
    total, categories = calculate_stats([])
    assert total == 0
    assert categories == {}

# Test 4: Handling single items
def test_single_item():
    data = [{'category': 'Ads', 'amount': '25.50'}]
    total, _ = calculate_stats(data)
    assert total == 25.50

# Test 5: Float math check
def test_float_precision():
    data = [{'category': 'Ads', 'amount': '10.10'}, {'category': 'Ads', 'amount': '20.20'}]
    total, _ = calculate_stats(data)
    assert round(total, 2) == 30.30