class Factory(object):

    """Docstring for Factory. """

    @staticmethod
    def build_sequence():
        return []
        
    @staticmethod
    def build_number(string):
        return int(string)

from string import ascii_lowercase, digits

class TextInput (object):
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    @classmethod
    def check_name(cls, text):
        for x in text:
            if x not in cls.CHARS_CORRECT:
                return False
        return 3<len(text)<50

    def __init__(self, name, size):
        self.size = 10
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'><{self.name}>: <input type='text' size=<{self.size}> />" 

class PasswordInput (object):
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    @classmethod
    def check_name(cls, text):
        for x in text:
            if x not in cls.CHARS_CORRECT:
                return False
        return 3<len(text)<50

    def __init__(self, name, size):
        self.size = 10
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='password'><{self.name}>: <input type='text' size=<{self.size}> />" 


        
