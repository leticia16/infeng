import pytest, json
from Engine import Engine

def test_load_knowledge():
    with open('__test__/knowledge.json', 'r') as file:
        e = Engine(file)
    with open('__test__/knowledge.json', 'r') as file:
        jfile = json.load(file)
        rules = jfile['rules']

    value_C_rules = e.values_table['C'].is_right_side_in_rules
    value_E_rules = e.values_table['E'].is_right_side_in_rules

    for i in range(len(e.knowledge_base)):
        assert e.knowledge_base[i].left == rules[i][0]
        assert e.knowledge_base[i].right == rules[i][1]

    assert e.knowledge_base[0] == value_C_rules[0]
    assert e.knowledge_base[1] == value_E_rules[0]


