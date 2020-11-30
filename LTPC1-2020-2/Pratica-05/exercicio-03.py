# Exercício 3 - encontrar as raizes de uma equacao grau 2
a  =  float ( input ( 'Coeficiente A:' ))
b  =  float ( input ( 'Coeficiente B:' ))
c  =  float ( input ( 'Coeficiente C:' ))

#Potencia no python- x elevado ay == x ** y
delta  = ( b ** 2 ) - ( 4 * a * c )

#Determina o número de raiz em função do valor do delta
se  delta  <  0 :
  print ( 'Nao possui raizes reais' )
elif  delta  >  0 :
  x1  = ( - b  +  delta ** 0,5 ) / ( 2 * a )
  x2  = ( - b  -  delta ** 0,5 ) / ( 2 * a )
  imprimir ( 'Raizes:' , x1 , x2 )
mais :
  x2  = ( - b  -  delta ** 0,5 ) / ( 2 * a )
  imprimir ( 'Raiz:' , x2 )
