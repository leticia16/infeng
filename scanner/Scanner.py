import re
from .tokens import tokens

class Scanner(object):
    def __init__(self):
        self.sentence = ''
        self.pos = 0
        self.buffer = ''
        self.tokens = []

    def clean(self):
        self.sentence = ''
        self.pos = 0
        self.buffer = ''
        self.tokens = []

    def __add_buffer_to_tokens(self, group : str):
        self.tokens.append([self.buffer, group])
        self.buffer = ''

    def __add_to_tokens(self, lexema, group):
        self.tokens.append([lexema, group])

    def __handle_buffer(self):
        if self.buffer == '':
            return
        elif self.buffer == 'and' or self.buffer == 'or':
            self.__add_buffer_to_tokens(tokens.OPERATOR)
        elif re.compile(r'[A-Z][A-Za-z\d]*').match(self.buffer):
            self.__add_buffer_to_tokens(tokens.ID)
        else:
            raise Exception(f'Invalid token "{self.buffer}" at {self.sentence}')

    def __is_delimiter(self, charac):
        if charac in ['!', '(', ')']:
            self.__handle_buffer()
            if charac == '!':
                self.__add_to_tokens(charac, tokens.NOT)
            else:
                self.__add_to_tokens(charac, tokens.DELIMITER)
            return True
        return False

    def scan(self, sentence : str):
        self.sentence = sentence
        if re.compile(r'!\(').search(sentence):
            raise Exception('Invalid expression !(')
        for i in sentence:
            if self.__is_delimiter(i):
                pass
            elif i != ' ':
                self.buffer += i
            else:
                self.__handle_buffer()
        tokens_list =  self.tokens
        self.clean()
        return tokens_list

