from .alphabet import Alphabet, Vowels

class NameHundler:
    def __init__(self, name: str):
        self.name = name.lower().replace(' ', '')
        self.__alphabet = Alphabet(self.name)
    
    def _culc_number(self, name: str) -> int:
        res = sum(self.__alphabet.table[a] for a in name)
        while( res > 9):
            res = sum(int(a) for a in str(res))
        return res
    @property
    def number(self) -> int:
        return self._culc_number(self.name)
    
    @property
    def composite_number(self) -> int:
        res = sum(self.__alphabet.table[a] for a in self.name)
        while( res > 30):
            res = sum(int(a) for a in str(res))
        return res
    def _get_consonants(self) -> str:
        return self.name.translate( str.maketrans("", "", Vowels[self.__alphabet.language.name].value))
    @property
    def individ_number(self) -> int:
        return self._culc_number(self._get_consonants())