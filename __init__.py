from ctypes import set_last_error
import os
from typing import List

class Money:
    """description"""
    def __init__(self, money):
        self.money=money
        
class Point:
    """stepok 1_4"""
    def __init__(self, x, y,color ='black'):
        """TODO: Docstring for __init__.
        :arg1: TODO
        :returns: TODO
        """
        self.x=x
        self.y=y
        self.color=color

points=[]
for obj in range(0,2000,2):
    points.append(Point(obj, obj))

points[1].color='yellow'

#!/usr/bin/env python
import random

class Line:
    """description"""
    def __init__(self, a,b,c,d):
        self.sp=(a,b)
        self.ep=(c,d)

    def nullifire(self):
        """Set nulls into class attr
        """
        self.sp=(0,0)
        self.ep=(0,0)

class Rect:
    """description"""
    def __init__(self, a,b,c,d):
        self.sp=(a,b)
        self.ep=(c,d)
        
class Elipse:
    """description"""
    def __init__(self, a,b,c,d):
        self.sp=(a,b)
        self.ep=(c,d)
elements=[]
for i in range(0,217,1):
    a = random.randrange(0,100,1)
    b = random.randrange(0,100,1)
    c = random.randrange(0,100,1)
    d = random.randrange(0,100,1)
    elements.append(random.choice([Line(a,b,c,d), Rect(a,b,c,d), Elipse(a,b,c,d)]))

for nums in elements:
    if isinstance(nums, Line):
        nums.nullifire()

#!/usr/bin/env python3

class Graph:
    """description"""
    def __init__(self, args):
        self.data=args
        self.is_show=True
        self.strdata= " ".join(map(lambda x: str(x), self.data))

    def set_data(self, args):
        self.data=args
    
    def show_table(self):
        if self.is_show==True:
            print(*self.data)
        else:
            print('Отображение данных закрыто')
 
    def show_graph(self):
        if self.is_show==True:
            print(f'Графическое отображение данных:{self.strdata}')
        else:
            print('Отображение данных закрыто')
        
    def show_bar(self):
        if self.is_show==True:
            print(f'Столбчатая диаграмма:{self.strdata}')
        else:
            print('Отображение данных закрыто')

    def set_show(self,fl_show):
        self.is_show=fl_show

data_graph = [1,4,5,667]
gr=Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()

#!/usr/bin/env python3

class CPU:
    """description"""
    def __init__(self, name, fr):
        self.name=name
        self.fr=fr
        
class Memory:
    """description"""
    def __init__(self, name, volume):
        self.name=name
        self.volume=volume

    def _get(self):
        return f'{self.name} - {self.volume}'
        
class MotherBoard:
    """description"""
    def __init__(self, name, cpu, *args):
        self.name=name
        self.cpu=cpu
        self.slot=4
        self.mem=args[:self.slot]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
               f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
               f'Слотов памяти: {self.slot}',
               f'Память:'+'; '.join(map(lambda x: x._get(), self.mem))]
       
#!/usr/bin/env python3

class Cart(object):

    """Docstring for Cart. """

    def __init__(self, __goods=[]):
        """TODO: to be defined. """
        self.goods=__goods

    def add(self, gr):
        self.goods.append(gr)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]
        
class Sells(object):
    """Docstring for Sells. """

    def __init__(self, name, price):
        self.name=name
        self.price=price

class Table(Sells):
    pass
class TV(Sells):
    pass
class Notebook(Sells):
    pass
class Cup(Sells):
    pass

tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)
cart=Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
#!/usr/bin/env python
import random

class Cell(object):

    """Docstring for Cell. """

    def __init__(self, around_mine=0):
        """TODO: to be defined. """
        self.mine=False
        self.around_mine=around_mine
        self.fl_open=False

    def set_mine(self):
        self.mine=True
        
class GamePole(object):

    """Docstring for GamePole. """

    def __init__(self, N, M):
        """TODO: to be defined. """
       random. 
