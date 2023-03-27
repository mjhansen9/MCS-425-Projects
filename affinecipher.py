#personal creation to aide me in my assignments for a cryptography course I took. Used to help decode affine ciphers

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
    
#print(gcd(2,4))

def numerify(X):
    X=X.lower()
    a=[]
    for i in range(0,len(X)):
        if X[i]=='a':
            a.append(0)
        if X[i]=='b':
            a.append(1)
        if X[i]=='c':
            a.append(2)
        if X[i]=='d':
            a.append(3)
        if X[i]=='e':
            a.append(4)
        if X[i]=='f':
            a.append(5)
        if X[i]=='g':
            a.append(6)   
        if X[i]=='h':
            a.append(7)
        if X[i]=='i':
            a.append(8)    
        if X[i]=='j':
            a.append(9)  
        if X[i]=='k':
            a.append(10)
        if X[i]=='l':
            a.append(11)   
        if X[i]=='m':
            a.append(12)   
        if X[i]=='n':
            a.append(13)
        if X[i]=='o':
            a.append(14)
        if X[i]=='p':
            a.append(15)
        if X[i]=='q':
            a.append(16)
        if X[i]=='r':
            a.append(17)
        if X[i]=='s':
            a.append(18)
        if X[i]=='t':
            a.append(19)
        if X[i]=='u':
            a.append(20)
        if X[i]=='v':
            a.append(21)
        if X[i]=='w':
            a.append(22)
        if X[i]=='x':
            a.append(23)
        if X[i]=='y':
            a.append(24)
        if X[i]=='z':
            a.append(25)
    return a


#print(numerify('abczyx'))


def denumerify(X):
    a=''
    for i in range(0,len(X)):
        if X[i]==0:
            a+='a'
        if X[i]==1:
            a+='b'  
        if X[i]==2:
            a+='c'
        if X[i]==3:
            a+='d'
        if X[i]==4:
            a+='e'
        if X[i]==5:
            a+='f'
        if X[i]==6:
            a+='g'
        if X[i]==7:
            a+='h'
        if X[i]==8:
            a+='i'
        if X[i]==9:
            a+='j'
        if X[i]==10:
            a+='k'
        if X[i]==11:
            a+='l'
        if X[i]==12:
            a+='m'
        if X[i]==13:
            a+='n'
        if X[i]==14:
            a+='o'
        if X[i]==15:
            a+='p'
        if X[i]==16:
            a+='q'
        if X[i]==17:
            a+='r'
        if X[i]==18:
            a+='s'
        if X[i]==19:
            a+='t'
        if X[i]==20:
            a+='u'
        if X[i]==21:
            a+='v'
        if X[i]==22:
            a+='w'
        if X[i]==23:
            a+='x'
        if X[i]==24:
            a+='y'
        if X[i]==25:
            a+='z'
    return a
    
    
#print(denumerify([1,24,25]))

def affinedecrypt(X):
    X=X.lower()
    X1=numerify(X)
    forfile=[]
    for m in range(1,25):
        if gcd(m,26)==1:
            for b in range(1,25):
                a=[]
                for i in range(len(X1)):
                    y=m*(X1[i]-b)
                    z=y%26
                    a.append(z)
                final=denumerify(a)
                print(m,b)
                print(final)
                forfile.append(final)
                
                
#affinedecrypt('cor')

#affinedecrypt('ycvejqwvhqtdtwvwu')    