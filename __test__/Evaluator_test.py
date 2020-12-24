import pytest
from Evaluator import Evaluator
from Engine import Engine


def asking(ansewer):
    def respond(value):
        value.value = ansewer
    return respond


def test_evaluate():
    ev = Engine('__test__/knowledge.json').evaluator
    ev2 = Engine('__test__/knowledge.json').evaluator
    ev3 = Engine('__test__/knowledge.json').evaluator
    ev4 = Engine('__test__/knowledge.json').evaluator
    ev.ask_for = asking(True)
    ev2.ask_for = asking(True)
    ev3.ask_for = asking(True)
    ev4.ask_for = asking(True)

    result = ev.evaluate('J')
    result2 = ev2.evaluate('!B')
    result3 = ev3.evaluate('E')
    result4 = ev4.evaluate('F')

    del ev4.values_table['A']

    result5 = ev4.evaluate('G')
    result6 = ev3.evaluate('H')
    result7 = ev3.evaluate('I')


    assert result == True, 'ask for value'
    assert result2 == False, 'denial B'
    assert result3 == False, 'looks for rules to solve E'
    assert result4 == True, 'evaluation recursion'
    assert result5 == False, 'if expression already solved just get its value'
    assert result6 == False, 'Bigger and expression'
    assert result7 == True, 'Bigger or expression'

