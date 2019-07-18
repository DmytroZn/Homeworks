# bencoding
# http://www.bittorrent.org/beps/bep_0003.html

"""
Strings are length-prefixed base ten followed by a colon and the string.
For example 4:spam corresponds to 'spam'.

>>> encode(b'spam')
b'4:spam'

Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
For example i3e corresponds to 3 and i-3e corresponds to -3.
Integers have no size limitation. i-0e is invalid.
All encodings with a leading zero, such as i03e, are invalid,
other than i0e, which of course corresponds to 0.

>>> decode(b'i3e')
3
>>> decode(b'i-3e')
-3
>>> decode(b'i0e')
0
>>> decode(b'i03e')
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 0: '03'
 

Lists are encoded as an 'l' followed by their elements (also bencoded) followed by an 'e'.
For example l4:spam4:eggse corresponds to ['spam', 'eggs'].

>>> decode(b'l4:spam4:eggse')
[b'spam', b'eggs']

Dictionaries are encoded as a 'd' followed by a list of alternating keys
and their corresponding values followed by an 'e'.
For example, d3:cow3:moo4:spam4:eggse corresponds to {'cow': 'moo', 'spam': 'eggs'}
Keys must be strings and appear in sorted order (sorted as raw strings, not alphanumerics).

>>> decode(b'd3:cow3:moo4:spam4:eggse')
OrderedDict([(b'cow', b'moo'), (b'spam', b'eggs')])

"""

from itertools import *
import re
import string

def encode(val):
  
  if isinstance(val, int):
    return 'i'+ str(val)+'e'
  elif isinstance(val, bytes):
    return str(len(val)) + ':' + val
  elif isinstance(val, list):
    return 'l' +''.join(map(encode, val)) + 'e'
  elif isinstance(val, dict):
    itemss =list(val.items())
    return 'd'+''.join(map(encode, chain(*itemss)))+'e'   # make from [('a','b'),('c','d')] =>['a','b','c','d'] it`s depend on 'chain(*itemss)'
  raise ValueError ('Write only: bytes,int, list or dict')

 
def decode(val):

  def dec_new(s):
    if s.startswith("i"):
      rez = re.match("i(-?\d+)e", s)
      return int(rez.group(1)), s[rez.span()[1]:] 

    elif s.startswith("l") or s.startswith("d"):
      l = []
      rest = s[1:]
      while not rest.startswith("e"):
        elem, rest = dec_new(rest)     
        l.append(elem)
      rest = rest[1:]
      if s.startswith("l"):
        return l, rest
      else:
        return {i: j for i, j in zip(l[::2], l[1::2])}, rest
    elif any(s.startswith(i.encode()) for i in string.digits):
      m = re.match("(\d+):", s)
      length = int(m.group(1))
      rest_i = m.span()[1]
      start = rest_i
      end = rest_i + length
      return s[start:end], s[end:]
    else:
      raise ValueError ('You wrote not correct values')

  ret, rest = dec_new(val)   
  if rest:
    raise ValueError ('You wrote not correct values')
  return ret




if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)    