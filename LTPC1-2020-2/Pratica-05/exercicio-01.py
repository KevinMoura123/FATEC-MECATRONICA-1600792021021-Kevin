#exercicio 1 - aula 5

A  =  int ( input ( 'Digite o valor do A:' ))
B  =  int ( input ( 'Digite o valor do B:' ))
C  =  int ( input ( 'Digite o valor do C:' ))

se  A  > =  B  e  A  > =  C :
  maior  =  A
elif  B  > =  A  e  B  > =  C :
  maior  =  B
mais :
  maior  =  C

se  A  <=  B  e  A  <=  C :
  menor  =  A
elif  B  <=  A  e  B  <=  C :
  menor  =  B
mais :
  menor  =  C

print ( "Maior valor:" , maior )
imprimir ( 'Menor valor:' , menor )

mídia  = ( A  +  B  +  C ) /  3
imprimir ( 'Valor médio:' , mídia )
