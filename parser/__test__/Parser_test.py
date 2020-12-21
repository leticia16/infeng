import pytest
from parser import Parser
from scanner import tokens, Scanner

# A and (!B and (C or B))
token_list = [['A', tokens.ID], ['and', tokens.OPERATOR],
           ['(', tokens.DELIMITER], ['!', tokens.NOT],
           ['B', tokens.ID], ['and', tokens.OPERATOR],
           ['(', tokens.DELIMITER], ['C', tokens.ID],
           ['or', tokens.OPERATOR], ['B', tokens.ID],
           [')', tokens.DELIMITER], [')', tokens.DELIMITER]]


def test_stack():
    p = Parser()
    p.push_stack('not')
    p.push_stack('and')

    assert p.stack_top() == 'and'
    assert p.pop_stack() == 'and'

def test_queue():
    p = Parser()
    p.push_queue('not')
    p.push_queue('and')

    assert p.pop_queue() == 'not'

def test_parse():
    p = Parser()
    s = Scanner()
    token_list1 = s.scan('A and (!B and (C or B))')
    token_list2 = s.scan('A and B and (C or B)')
    expected1 = [['A', 2], ['B', 2], ['!', 3], ['C', 2],
                ['B', 2], ['or', 1], ['and', 1], ['and', 1]]
    expected2 = [['A', 2], ['B', 2], ['and', 1], ['C', 2],
                ['B', 2], ['or', 1], ['and', 1]]

    result1 = p.parse(token_list1)
    result2 = p.parse(token_list2)

    assert result1 == expected1
    assert result2 == expected2

