#Calculadora Personalizada
# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisao

def  exibir_menu ():
  imprimir ( "Menu Calculadora:" )
  imprimir ( "1 - Somar" )
  imprimir ( "2 - Subtrair" )
  imprimir ( "3 - Multiplicar" )
  imprimir ( "4 - Dividir" )
  imprimir ( "0 - Sair" )

def  somar ( numero1 , numero2 ):
  retornar  numero1 + numero2

def  subtrair ( numero1 , numero2 ):
  return  numero1 - numero2

def  multiplicar ( numero1 , numero2 ):
  return  numero1 * numero2

def  dividir ( numero1 , numero2 ):
  se  numero2  ! =  0 :
    return  numero1 / numero2
  mais :
    return  "Divisão por zero!"

#Programa principal
importar  os
continuar  =  verdadeiro
enquanto  continuar  ==  Verdadeiro :
  os . sistema ( "limpar" ) #Sem janelas - cls
  exibir_menu ()
  opcao  =  int ( input ( "Opcao:" ))
  se  opcao  ==  1 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , somar ( n1 , n2 ))
  elif  opcao  ==  2 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    imprimir ( "Resultado:" , subtrair ( n1 , n2 ))
  elif  opcao  ==  3 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    imprimir ( "Resultado:" , multiplicar ( n1 , n2 ))
  elif  opcao  ==  4 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , dividir ( n1 , n2 ))
  elif  opcao  ==  0 :
    continuar  =  False
  mais :
    imprimir ( "Opcao Invalida!" )
  entrada ( "Pressione, insira para continuar" )
