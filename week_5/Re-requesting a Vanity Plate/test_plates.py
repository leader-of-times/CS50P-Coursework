from plates import is_valid

def main():
    test_plates()
    test_plates_number_between()
    test_plates_punctuation()
    test_plates_limit()
    test_no_value()
    test_invalid_start()
    test_zero_placement()

def test_plates():
    assert is_valid("CS50") == True

def test_plates_number_between():
    assert is_valid("CS50P") == False

def test_plates_punctuation():
    assert is_valid("PI3.14") == False

def test_plates_limit():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_no_value():
    assert is_valid("") == False

def test_invalid_start():
    assert is_valid("50CS") == False
    assert is_valid("1CS50") == False
    assert is_valid("C50S") == False
    assert is_valid("CS50P") == False

def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("AB010C") == False

if __name__ == "__main__":
    main()
