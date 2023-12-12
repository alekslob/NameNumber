from enum import Enum

class Message(str, Enum):
    ENTERNAME = "Введите имя: "
    UNKNOWCHAR = "Буква из неизвестного алфавита"