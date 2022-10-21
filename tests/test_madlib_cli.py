import pytest
from madlib_cli.madlib_cli import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected



def test_parse_template():
    read_file = read_template("assets/dark_and_stormy_night_template.txt")
    actual_parts, regular_expression = parse_template(read_file)
        
    
    regular_expression = "{.[^}]*}"
    expected_parts = ["{Adjective}", "{Adjective}", "{Noun}"]
    

    assert regular_expression == regular_expression
    assert actual_parts == expected_parts


def test_merge():
    read_file = read_template("assets/dark_and_stormy_night_template.txt")
    actual = merge("assets/dark_and_stormy_night_template.txt", ["dark", "stormy", "night"], "{.[^}]*}", read_file )
    expected = (['dark', 'stormy', 'night'], 'It was a dark and stormy night.')
    assert actual == expected



def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)