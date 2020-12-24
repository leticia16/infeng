import pytest, json
from contextlib import contextmanager
from Engine import Engine
from Value import Value

@contextmanager
def engine_context():
    e = Engine('__test__/knowledge.json')
    file = open('__test__/knowledge.json', 'r')
    try:
        yield e, json.load(file)
    finally:
        file.close()


def test_load_descriptions():
    with engine_context() as (e, jfile):
        desc = jfile['description']

    for key in desc.keys():
        value = e.values_table[key]
        if type(desc[key]) == list:
            assert value.value == desc[key][0]
            assert value.description == desc[key][1]
        else:
            assert value.value == desc[key]

def test_load_rules():
    with engine_context() as (e, jfile):
        rules = jfile['rules']

        for i in range(len(e.knowledge_base)):
            assert e.knowledge_base[i].left == rules[i][0]
            assert e.knowledge_base[i].right == rules[i][1]



