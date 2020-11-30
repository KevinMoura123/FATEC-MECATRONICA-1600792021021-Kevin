#Exercicio 4 - Calculadora 4 operacoes basicas
operacao  =  input ( 'Informe a operacao desejada:' )

se  operacao  ==  '+' :
  valor1  =  float ( input ( 'Valor 1:' ))
  valor2  =  float ( input ( 'Valor 2:' ))
  resultado  =  valor1  +  valor2
  imprimir ( resultado )
elif  operacao  ==  '-' :
  valor1  =  float ( input ( 'Valor 1:' ))
  valor2  =  float ( input ( 'Valor 2:' ))
  resultado  =  valor1  -  valor2
  imprimir ( resultado )
elif  operacao  ==  '*' :
  valor1  =  float ( input ( 'Valor 1:' ))
  valor2  =  float ( input ( 'Valor 2:' ))
  resultado  =  valor1  *  valor2
  imprimir ( resultado )
elif  operacao  ==  '/' :
  valor1  =  float ( input ( 'Valor 1:' ))
  valor2  =  float ( input ( 'Valor 2:' ))
  se  valor2  ==  0 :
    print ( 'Tentativa de divisão por zero!' )
  mais :
    resultado  =  valor1  /  valor2
    imprimir ( resultado )
mais :
  imprimir ( 'Operacao inválida!' )
