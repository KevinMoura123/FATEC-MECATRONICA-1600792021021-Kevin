menor_preco  =  float ( 'inf' )
melhor_loja  =  ''

continuar  =  verdadeiro

enquanto  continuar  ==  Verdadeiro :
  preco  =  float ( input ( "Preco:" ))
  loja  =  input ( "Loja:" )
  se  preco  <  menor_preco :
    menor_preco  =  preco
    melhor_loja  =  loja
  continuar  =  entrada ( "Deseja continuar?" ). inferior () ==  's'

print ( "Melhor loja:% s com o preço R $%. 2f"  % ( melhor_loja , menor_preco ))
