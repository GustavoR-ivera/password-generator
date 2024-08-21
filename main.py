import random

def isSpecialCharacter(value):
    list = ['$','%','&','#','@','!','?','¿','¡']
    if value in list:
        return True
    else:
        return False

def isLowerCase(value):
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    if value in list:
        return True
    else:
        return False

def isCapitalLetter(value):
    list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if value in list:
        return True
    else:
        return False

def passwordGenerator(n):
    m=n
    password = ''
    set = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,' \
          'z,0,1,2,3,4,5,6,7,8,9,$,%,&,#,@,!,?,¿,¡'
    haveSpecialCharacter = False
    haveNumber = False
    haveLowerCase = False
    haveCapitalLetter = False
    list = set.split(',')

    while n>0:
        i = random.randint(0, len(list)-1)
        value = list[i]

        if(isSpecialCharacter(value)):
            haveSpecialCharacter = True
        elif(value.isdigit()):
            haveNumber = True
        elif(isCapitalLetter(value)):
            haveCapitalLetter = True
        elif(isLowerCase(value)):
            haveLowerCase = True

        password = password + value
        n = n - 1

    passwordValidator(haveCapitalLetter,haveLowerCase,haveNumber,haveSpecialCharacter, password, m)

def passwordValidator(haveCapitalLetter, haveLowerCase, haveNumber, haveSpecialCharacter, password, m):
    #desempaquetamiento de la tupla "parametros"
    size = len(password)
    if(haveCapitalLetter and haveNumber and haveLowerCase and haveSpecialCharacter):
        print("contraseña generada: ", password)
    else:
        passwordGenerator(m)


def main():
    n=int(input("ingresa una longitud para tu contraseña (mínimo 4 caracteres, se recomiendan 8 o más)"))

    while n<4:
        print("no es posible generar una contraseña segura con menos de 4 caracteres")
        n = int(input("ingresa una longitud para tu contraseña (mínimo 4 caracteres, se recomiendan 8 o más)"))

    passwordGenerator(n)

main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
