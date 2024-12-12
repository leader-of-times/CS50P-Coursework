import pytest
import working

def test_convert_valid():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert working.convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        working.convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        working.convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        working.convert("9:00 AM to 5:00")

def test_convert_invalid_time():
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        working.convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        working.convert("9:00 AM to 13:00 PM")

def test_convert_edge_cases():
    assert working.convert("12:00 AM to 12:00 AM") == "00:00 to 00:00"
    assert working.convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
