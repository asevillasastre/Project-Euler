def cifras(n):
    cifras=[]
    while n>0:
        cifras.append(n%10)
        n=n//10
    return cifras

def palindromo(n):
    if len(cifras(n))==5:
        j=0
        while j!=2:

            ver= cifras(n)[j]==cifras(n)[4-j]
            j+=1
            if ver==False:
                return False
        return True
    if len(cifras(n))==6:
        j=0
        while j!=3:

            ver= cifras(n)[j]==cifras(n)[5-j]
            j+=1
            if ver==False:
                return False
        return True

a=999
b=100
c=0
animal=[]
#a<b
while a>0:
    while b<a:
        if palindromo(a*b)==True:
            animal.append(a*b)
        b+=1
    
    if palindromo(a*b)==True:
        animal.append(a*b)
    a-=1
    b=0
max(animal)