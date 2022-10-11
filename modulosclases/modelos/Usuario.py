#funcion sin parametros ni retorno
def funcionSumar():
    print(10+15)    
    ''' print(funcionSumar())  '''

#funcion con parametros requeridos
def funcionSumar2(num1,num2):
    ''' print(funcionSumar2(10,23))  '''
    return num1+num2
      
   
#funcion con parametros opcionales (valores por defecto)
def potencias(num=13,poten=5): 
    ''' print(potencias())
    print(potencias(10))
    print(potencias(poten=4))
    print(potencias(3,6))
    print(potencias(poten=3,num=6)) '''
    return num ** poten

#funcion con varios retornos(retorno Tupla)
def tablasMultiplic(num1):
    return num1*2,num1*3,num1*4,num1*5,num1*6    

#print(tablasMultiplic(7))


def getMinombre():
    return (__name__)




