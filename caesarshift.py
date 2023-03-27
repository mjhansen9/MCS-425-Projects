#personal creation to aide me in my assignments for a cryptography course I took. Used to help decode caesar ciphers

def caesar_shift(x):
    """takes in a string of cipher text and performs all 26 possible shifts to attempt to decrypt it"""
    x=x.lower()
    for i in range(26):
        a=''
        for q in range(len(x)):
            y=ord(x[q])+i
            if y<=122:
                z=chr(y)
            else:
                z=chr(y-26)
            a+=z
        print(a)
            
            
#caesar_shift('ycvejquvhqtdtwvwu')
#ycvejquvhqtdtwvwu
caesar_shift('sqji')