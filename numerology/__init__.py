from .name_hundler import NameHundler
from .messages import Message
from .exception import *
def start():
    while(True):
        try:
            name = input(Message.ENTERNAME.value)
            if name!='':
                print(NameHundler(name).number)
        except UnknowChar:
            print(Message.UNKNOWCHAR.value)