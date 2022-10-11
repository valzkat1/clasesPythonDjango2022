# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	operacion = int()
	num1 = int()
	num2 = int()
	resultado = float()
	print("Seleccione la operación que desea realizar")
	print("1.Samar")
	print("2.Restar")
	print("3.Multiplicar")
	print("4.Dividir")
	print("5.Salir")
	operacion = int(input())
	print("Por favor ingrese el primer numero")
	num1 = int(input())
	print("Por favor ingrese el segundo numero")
	num2 = int(input())
	if operacion==4:
		while num2==0:
			print("Por favor ingresar de nuevo el segundo numero(No se permite el 0)")
			num2 = int(input())
	if operacion==1:
		resultado = num1+num2
	if operacion==2:
		resultado = num1-num2
	if operacion==3:
		resultado = num1*num2
	if operacion==4:
		resultado = num1/num2
	print("El resultado es: ",resultado)

