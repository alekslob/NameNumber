from .alphabet import Alphabet, Vowels

class NameHundler:
    def __init__(self, name: str):
        self.name = name.lower().replace(' ', '')
        self.__alphabet = Alphabet(self.name)
    

    @property
    def number(self) -> int:
        res = sum(self.__alphabet.table[a] for a in self.name)
        while( res > 9):
            res = sum(int(a) for a in str(res))
        return res
    
    @property
    def composite_number(self) -> int:
        res = sum(self.__alphabet.table[a] for a in self.name)
        while( res > 30):
            res = sum(int(a) for a in str(res))
        return res
    
    @property
    def consonants(self) -> str:
        return self.name.translate( str.maketrans("", "", Vowels[self.__alphabet.language.name].value))
    
    @property
    def individ_number(self) -> int:
        res = sum(self.__alphabet.table[a] for a in self.consonants)
        while(res is not 22 and res is not 11 and res > 9):
            res = sum(int(a) for a in str(res))
        return res
    
    @property
    def vowels(self) -> str:
        return self.name.translate(str.maketrans("", "", self.consonants))

    @property
    def soul_number(self) -> int:
        res = sum(self.__alphabet.table[a] for a in self.vowels)
        while(res is not 22 and res is not 11 and res > 9):
            res = sum(int(a) for a in str(res))
        return res
    