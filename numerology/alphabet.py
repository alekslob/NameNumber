from .exception import *
from enum import Enum
class Language(Enum):
    eng = [chr(i) for i in range(97, 123)]
    ru = list([chr(i) for i in list(range(ord('а'), ord('е')+1)) + [ord('ё')] +list(range(ord('ж'), ord('я')+1))])

class Vowels(Enum):
    eng = 'aeiou'
    ru = 'аеёиоуэюя'

class Alphabet:

    def __init__(self, name: str):
        self.name = name
        self.__check_chars()
        
    def __check_chars(self):
        language = None
        for char in self.name:
            lang = None
            for l in list(Language):
                if char in l.value:
                    lang = l
                    break
            if lang is None:
                raise UnknowChar
            if language is None:
                language = lang
            if language is not lang:
                raise LanguageError
        self.language = language
        
    @property
    def table(self) -> dict:
        res = dict()
        i = 1
        for a in self.language.value:
            res[a] = i
            i+=1
            if i == 10: i =1
        return res
