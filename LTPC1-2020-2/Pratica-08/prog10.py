preco  =  input ( "Preço:" )
real  =  ""
centavos  =  ""
achei_virgula  =  False
para  caracter  in  preco :
  if  caracter  ! =  ',' :
    #COPIAR CARACTER
    if  achei_virgula  ==  False :
      real  =  real  +  caracter
    mais :
      centavos  =  centavos  +  caractere
  mais :
    achei_virgula  =  True

if  achei_virgula  ==  True :
  imprimir ( "Reais:" , reais , "Centavos:" , centavos )
mais :
  imprimir ( "Reais:" , real )
