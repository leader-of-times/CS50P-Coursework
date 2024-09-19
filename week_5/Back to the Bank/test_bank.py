from bank import value  # Import the value function from bank module

def main():
    test_value()

def test_no_value():
    assert value("") == 100  # Use value directly

def test_value():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100

def test_number_value():
    assert value("20") == 100
