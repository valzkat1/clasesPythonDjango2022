

from excepcionPropia import excepcionPropia


def solicitarDato():
    print("Por favor ingrese el numero de años")
    dato=int(input())
    if dato<1:        
        raise excepcionPropia("Solo numeros positivos")
    else:
        print("Cantidad correcta")


try:
  solicitarDato()
except excepcionPropia:
    print("Error de data")    