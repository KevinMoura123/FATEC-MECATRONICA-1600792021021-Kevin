def  contarPalavras ( frase , palavra ):
  total  =  0
  para  palavra_na_frase  na  frase . dividir ( "" ):
    if  palavra_na_frase  ==  palavra :
      total  =  total  +  1
  retorno  total


frase  =  input ( "Informe uma frase:" )
alvo  =  input ( "Informe uma palavra para contar:" )
imprimir ( contarPalavras ( frase , alvo ))
