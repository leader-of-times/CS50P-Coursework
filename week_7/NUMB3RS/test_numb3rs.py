import pytest
from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_ipv4():
    assert validate("256.0.0.0") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168..1") == False

if __name__ == "__main__":
    pytest.main()
