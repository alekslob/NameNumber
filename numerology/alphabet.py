from .exception import *

eng = [chr(i) for i in range(97, 123)]
ru =  [chr(i) for i in range(1072, 1104)]
ru.insert(6, 'ё')

class Alphabet:
    def __init__(self, char: str):
        self.char = char

    @property
    def lang(self) -> list:
        if ru.__contains__(self.char):
            return ru
        if eng.__contains__(self.char):
            return eng
        raise UnknowChar("Буква из неизвестного алфавита")
    @property
    def table(self) -> dict:
        res = dict()
        i = 1
        for a in self.lang:
            res[a] = i
            i+=1
            if i == 10: i =1
        return res
