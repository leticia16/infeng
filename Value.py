

class Value(object):
    """This class keeps the values and the associated rules of a variable
    """
    NULL = 0

    def __init__(self, name, description='None', value=0):
        self.value = value
        self.is_right_side_in_rules = []
        self.description = description

    def was_defined(self):
        return self.value != 0

    def add_rule(self, rule):
        self.is_right_side_in_rules.append(rule)

