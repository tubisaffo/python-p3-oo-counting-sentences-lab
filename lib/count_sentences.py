#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) != str:
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return True if self.value.endswith(".") else False

    def is_question(self):
        return True if self.value.endswith("?") else False

    def is_exclamation(self):
        return True if self.value.endswith("!") else False

    def count_sentences(self):
        str_list = self.value.split(" ")
        count = 0
        for i in str_list:
            if i.endswith(".") or i.endswith("?") or i.endswith("!"):
                count += 1
        return count