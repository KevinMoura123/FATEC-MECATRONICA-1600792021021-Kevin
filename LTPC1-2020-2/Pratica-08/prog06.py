preco  =  input ( "Informe um preço:" )

posicao  =  0
posicao_da_virgula  =  - 1
enquanto  posicao  <  len ( preco ):
  if  preco [ posicao ] ==  ',' :
    posicao_da_virgula  =  posicao
  posicao  =  posicao  +  1

print ( "O valor prestado foi de" , preco [: posicao_da_virgula ], "reais" )
print ( "com" , preco [ posicao_da_virgula + 1 :], "centavos" )
