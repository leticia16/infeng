import json
from Rule import Rule
from Value import Value
from scanner import Scanner
from parser import Parser


class Engine(object):
    def __init__(self, knowledge_file):
        self.knowledge_base = []
        self.values_table = {}
        self.evaluator = None
        self.load_knowledge(knowledge_file)

    def __load_file_content(self, file):
        file = json.load(file)
        desc = file['description']
        rules = file['rules']
        return desc, rules

    def load_knowledge(self, file):
        desc, rules = self.__load_file_content(file)
        print('Loading descriptions...')
        for key in desc.keys():
            self.values_table[key] = Value(key, desc[key])
        print('Loading rules...')
        for i in rules:
            rule = Rule(i)
            self.knowledge_base.append(rule)
            # associa uma um valor (A) às regras nas quais ele
            # aparece no lado direito de uma regra
            self.values_table[rule.right].add_rule(rule)

