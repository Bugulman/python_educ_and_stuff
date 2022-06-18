
class Money:
    """description"""
    def __init__(self, money):
        self.money=money
        

class Point:
    """description"""
    color='black'
    def __init__(self, x, y, *arg1):
        """TODO: Docstring for __init__.
        :arg1: TODO
        :returns: TODO
        """
        self.x=x
        self.y=y
        self.color=arg1[0]
