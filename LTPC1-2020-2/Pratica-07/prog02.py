#Guarda a somatoria dos valores informados
somatoria  =  0
#Conta a quantidade de valores informados
contador  =  0
#Guarda o maior valor rede
maior  =  0
#Guarda o menor valor.
menor  =  0
#COnstroi a lógica de repetição - enquanto se mantiver verddaeiro, repete o código
continuar  =  verdadeiro
enquanto  continuar  ==  Verdadeiro :
  valor  =  int ( input ( "Valor:" ))
  #Adiciona o valor na somatoria
  somatoria  + =  valor  #somatoria = somatoria + valor
  #Adiciona mais um na contagem
  contador  + =  1  #contador = contador + 1
  #Para verificar se é oprimeiro numero Internet
  if  contador  ==  1 :
    maior  =  valor
    menor  =  valor
  mais :
    se  valor  >  maior :
      maior  =  valor
    elif  valor  <  menor :
      menor  =  valor
  #Verifica se o usuário deseja continuar
  continuar  =  input ( "Continuar?" ) ==  's'

media  =  somatoria / contador
imprimir ( "Mídia:" , mídia )
print ( "Maior:" , maior )
imprimir ( "Menor:" , menor )
