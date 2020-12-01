nome  =  input ( "Informe seu nome:" )
valor  =  float ( input ( "Informe um valor:" ))
numero_conta  =  input ( "Informe o número da conta:" )

validacao  =  input ( "String de validacao:" )
#escrever nome e numero da conta, separados por ";"

nome_validacao , numero_conta_validacao  =  validacao . dividir ( ';' )

if  nome  ==  nome_validacao  e  numero_conta  ==  numero_conta_validacao :
  print ( "Dados validados!" )
mais :
  print ( "Dados incorretos informados!" )
