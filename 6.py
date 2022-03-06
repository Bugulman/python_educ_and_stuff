import pdb

def create_phone_number(n):
    pdb.set_trace()
    n=[str(x) for x in n]
    number='({}) {}-{}'.format(''.join(n[0:3]), ''.join(n[4:7]), ''.join(n[7:-1]))
    return number


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
