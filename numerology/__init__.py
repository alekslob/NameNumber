from .name_hundler import NameHundler
from .messages import Message
from .exception import *
def start():
    while(True):
        try:
            name = input(Message.ENTERNAME.value)
            if name!='':
                print(Message.YOURNUMBER.value.format(NameHundler(name).number))
                print(Message.YOURCOMPOSITENUMBER.value.format(NameHundler(name).composite_number))
                print(Message.YOURINDIVIDNUMBER.value.format(NameHundler(name).individ_number))
        except UnknowChar:
            print(Message.UNKNOWCHAR.value)
        except LanguageError:
            print(Message.LANGUAGEERROR.value)

from .alphabet import Language, Vowels
def test():
    name="Владислав"
    print(NameHundler(name)._get_consonants())