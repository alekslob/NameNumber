from enum import Enum

class Message(str, Enum):
    ENTERNAME = "Введите имя: "
    YOURNUMBER = "Число имени: {}"
    YOURCOMPOSITENUMBER = "Составное число: {}"
    YOURINDIVIDNUMBER = "Индивидуальное число: {}"
    YOURSOULNUMBER = "Число души: {}"
    UNKNOWCHAR = "Буква из неизвестного алфавита"
    LANGUAGEERROR = "Буквы должны быть из одного алфавита"
