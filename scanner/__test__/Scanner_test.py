import pytest
from scanner import Scanner, tokens


s = Scanner()

def test_clean():
    s.sentence = 'A and B'
    s.buffer = 'and'
    s.tokens = [['A', tokens.ID]]

    s.clean()

    assert s.buffer == ''
    assert s.sentence == ''
    assert s.tokens == []


def test_add_buffer_to_tokens():
    s.clean()
    s.buffer = 'and'

    s._Scanner__add_buffer_to_tokens(tokens.OPERATOR)

    assert s.tokens == [['and', tokens.OPERATOR]]


def test_add_to_tokens():
    s.clean()
    token = ['A1', tokens.OPERATOR]

    s._Scanner__add_to_tokens(*token)

    assert s.tokens == [token]


def test_handle_buffer():
    s.clean()
    t1 = ['and', tokens.OPERATOR]
    t2 = ['Var', tokens.ID]

    s.buffer = t1[0]
    s._Scanner__handle_buffer()
    assert t1 in s.tokens

    s.buffer = t2[0]
    s._Scanner__handle_buffer()
    assert t2 in s.tokens

    with pytest.raises(Exception):
        s.buffer = 'ex'
        s._Scanner__handle_buffer()


def test_scan():
    s.clean()
    sentence = 'A and (B and (C or B and !D))'
    sentence2 = '!A'
    sentence3 = 'A and (B and !(C or B and D))'
    sentence4 = '1A and C'
    out = [['A', tokens.ID], ['and', tokens.OPERATOR],
           ['(', tokens.DELIMITER],
           ['B', tokens.ID], ['and', tokens.OPERATOR],
           ['(', tokens.DELIMITER], ['C', tokens.ID],
           ['or', tokens.OPERATOR], ['B', tokens.ID],
           ['and', tokens.OPERATOR], ['!', tokens.NOT],
           ['D', tokens.ID],
           [')', tokens.DELIMITER], [')', tokens.DELIMITER]]

    out2 = [['!', tokens.NOT], ['A', tokens.ID]]

    result = s.scan(sentence)
    result2 = s.scan(sentence2)

    assert out == result
    assert out2 == result2
    with pytest.raises(Exception):
        s.scan(sentence3)
        s.scan(sentence4)



