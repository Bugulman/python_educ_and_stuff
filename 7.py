import pdb
from loguru import logger
import snoop

@snoop
def isPP(n):
    for i in reversed(range(1, 1000)):
        a = n**(1/i)
        if int(a)/float(a)==1.0:
            if i==1:
                return None
            else:
                print(int(a), i)
                return (int(a), i)
                break
isPP(216)
