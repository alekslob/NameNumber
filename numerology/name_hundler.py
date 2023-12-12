from .alphabet import Alphabet

class NameHundler:
    def __init__(self, name: str):
        self.name = name.lower().replace(' ', '')
    
    @property
    def number(self) -> int:
        alph = Alphabet(self.name[0])
        res = sum(alph.table[a] for a in self.name)
        while( res > 9):
            res = sum(int(a) for a in str(res))
        return res