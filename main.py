"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y


def quadratic_multiply(x, y):
  return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    if (len(x.binary_vec) > 1 or len(y.binary_vec) > 1):
      x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)
    n = len(x.binary_vec)
    if not (n > 1):
      return BinaryNumber(x.decimal_val & y.decimal_val)

    xleft, xright = split_number(x.binary_vec)
    yleft, yright = split_number(y.binary_vec)

    l = bit_shift(_quadratic_multiply(xleft, yleft), n)

    mleft = _quadratic_multiply(xleft, yright)
    mright = _quadratic_multiply(xright, yleft)
  
    m = bit_shift(BinaryNumber(mleft.decimal_val + mright.decimal_val), n//2)

    r = _quadratic_multiply(xright, yright)

    return BinaryNumber(l.decimal_val + m.decimal_val + r.decimal_val)
    ###



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000


    
    

