"""
Description:

Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
"""

class CaesarCipher(object):
    letters = {k: chr(ord('a') + k).upper() for k in range(26)}
    def __init__(self, shift):
        self.ciper = shift
    
    @classmethod
    def shift_letter(cls, letter, shift):
        letter = letter
        if letter.upper() in cls.letters.values():
            return cls.letters[(ord(letter.upper()) - ord('A') + shift)%26]
        else:
            return letter

    def encode(self, string):
        return ''.join(self.shift_letter(l, self.ciper) for l in string)
        
    def decode(self, string):
        return ''.join(self.shift_letter(l, -self.ciper) for l in string)
        
        
a = CaesarCipher(5)

a.encode('Codewars')
a.decode('HTIJBFWX')

a.decode('BFKKQJX')


a.encode('eiya!!')


# others solutions
from string import maketrans
class CaesarCipher(object):
    
    def __init__(self, shift):
        self.alpha = "abcdefghijklmnopqrstuvwxyz".upper()
        self.newalpha = self.alpha[shift:] + self.alpha[:shift]
        

    def encode(self, str):
        t = maketrans(self.alpha, self.newalpha)
        return str.upper().translate(t)
            
            
        
    def decode(self, str):
        t = maketrans(self.newalpha, self.alpha)
        return str.upper().translate(t)