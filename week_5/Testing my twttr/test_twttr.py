from twttr import shorten

def test_no_vowels():
    assert shorten("noufal") == "nfl"

def test_capitalized_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello") == "Hll"

def test_numbers():
    assert shorten("abc123") == "bc123"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"


def test_empty_string():
    assert shorten("") == ""
