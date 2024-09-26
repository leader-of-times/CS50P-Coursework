import pytest
import um

def test_um_single():
    assert um.count("hello, um, world") == 1

def test_um_multiple():
    assert um.count("Um, thanks, um...") == 2

def test_um_case_insensitive():
    assert um.count("Um, thanks for the album.") == 1

def test_um_not_part_of_word():
    assert um.count("yummy") == 0

def test_um_surrounded_by_spaces():
    assert um.count("hello um world") == 1

def test_um_surrounded_by_punctuation():
    assert um.count("um?") == 1

def test_um_at_beginning():
    assert um.count("um, thanks for the album.") == 1

def test_um_at_end():
    assert um.count("hello, um") == 1

def test_um_empty_string():
    assert um.count("") == 0
