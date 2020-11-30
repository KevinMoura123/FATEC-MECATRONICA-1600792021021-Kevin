#Estrutura de repetição
numero_secreto  =  42

acertou  =  False
while  acertou  ==  False :
  chute  =  int ( input ( "Informe seu chute:" ))
  se  chute  >  numero_secreto :
    imprimir ( 'Errrrrrou por alto!' )
  elif  chute  <  numero_secreto :
    print ( "Errrou por baixo!" )
  mais :
    acertou  =  True
    imprimir ( "Acertou !!!" )

imprimir ( "Obrigado por jogar!" )
