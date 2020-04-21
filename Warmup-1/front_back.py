
#Given a string, return a new string where the first and last chars have been exchanged.


#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  if len(str) > 2:
    a = str[0]
    b = str[-1]
    new_str = b + str[1:-1] + a
    return new_str
  elif len(str) == 2:
    a = str[0]
    b = str[-1]
    new_str = b + a
    return new_str
  else:
    return str