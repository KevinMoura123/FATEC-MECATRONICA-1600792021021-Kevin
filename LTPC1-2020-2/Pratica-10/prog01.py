def  lerNumeroPositivo ():
  continuar  =  verdadeiro
  enquanto  continuar == Verdadeiro :
    numero  =  int ( input ( "Informe um valor:" ))
    continuar  =  numero  <  0  #condicao qo torna falso
  retorno  numero

primeiro_valor  =  lerNumeroPositivo ()
segundo_valor  =  lerNumeroPositivo ()
resposta  =  primeiro_valor  +  segundo_valor
print ( "A soma de" , primeiro_valor , "com" , segundo_valor , "é igual:" , resposta )

#Apenas somar 2 numeros se positivos
