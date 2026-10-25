from tally import count_text


def test_empty():
    c = count_text("")
    assert (c.lines, c.words, c.chars) == (0, 0, 0)


def test_trailing_newline():
    assert count_text("a b\nc\n").lines == 2


def test_no_trailing_newline():
    assert count_text("a b\nc").lines == 2
