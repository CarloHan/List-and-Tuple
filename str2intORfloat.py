from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def fn(x, y):
    return x * 10 + y
    
def char2num(s):
    return DIGITS[s]
    
def str2int(s):
    return reduce(fn, map(char2num, s))
  
def str2float(s):
    intNum, floatNum = s.split('.')
    intNum = reduce(fn, map(char2num, intNum))
    floatNum = reduce(fn, map(char2num, floatNum)) * (10**(-len(floatNum)))
    return intNum + floatNum
