#Calculadora Personalizada

def  xyz_menu ():
  print ( '1 - Resistência' )
  imprimir ( '2 - Tensão' )
  imprimir ( '3 - Corrente' )
  print ( '4 - Resistência Equivalente de circuito em Série' )
  print ( '5 - Resistência Equivalente de circuito em Paralelo' )
  imprimir ( '6 - Potência' )
  imprimir ( "0 - Sair" )

def  xyz_soma ( j_n1 , j_n2 ):
  retorno ( j_n1  +  j_n2 )

def  xyz_subtracao ( j_n1 , j_n2 ):
  retorno ( j_n1  -  j_n2 )

def  xyz_multiplicacao ( j_n1 , j_n2 ):
  retorno ( j_n1  *  j_n2 )

def  xyz_divisao ( j_n1 , j_n2 ):
  se  j_n2  ! =  0 :
    retorno ( j_n1  /  j_n2 )
  mais :
    retornar  "Impossível dividir por zero ..."

def  xyz_resistencia ( j_tensao , j_corrente ):
  return  xyz_divisao ( j_tensao , j_corrente )

def  xyz_tensao ( j_resistencia , j_corrente ):
  return  xyz_multiplicacao ( j_resistencia , j_corrente )

def  xyz_corrente ( j_tensao , j_resistencia ):
  return  xyz_divisao ( j_tensao , j_resistencia )

def  xyz_potencia ( j_res , j_corrente ):
  return ( j_res * ( j_corrente ** 2 ))

def  xyz_serie ( j_res_1 , j_res_2 ):
  retornar  xyz_soma ( j_res_1 , j_res_2 )

def  xyz_paralelo ( j_res_1 , j_res_2 ):
  return  xyz_divisao ( xyz_multiplicacao ( j_res_1 , j_res_2 ), xyz_soma ( j_res_1 , j_res_2 ))
  #return xyz_multiplicacao (j_res_1, j_res_2) / xyz_soma (j_res_1, j_res_2)

def  xyz_numeros ():
  v_1  =  float ( input ( "Valor 1:" ))
  v_2  =  float ( input ( "Valor 2:" ))
  retornar  v_1 , v_2

#Programa principal
importar  os
continuar  =  verdadeiro
enquanto  continuar  ==  Verdadeiro :
  os . sistema ( "limpar" )
  xyz_menu ()
  opcao  =  int ( input ( "Opcao:" ))
  se  opcao  ==  1 :
    n_1 , n_2  =  xyz_numeros ()
    print ( "Resultado:" , xyz_resistencia ( n_1 , n_2 ))
  elif  opcao  ==  2 :
    n_1 , n_2  =  xyz_numeros ()
    print ( "Resultado:" , xyz_tensao ( n_1 , n_2 ))
  elif  opcao  ==  3 :
    n_1 , n_2  =  xyz_numeros ()
    print ( "Resultado:" , xyz_corrente ( n_1 , n_2 ))
  elif  opcao  ==  4 :
    n_1 , n_2  =  xyz_numeros ()
    print ( "Resultado:" , xyz_serie ( n_1 , n_2 ))
  elif  opcao  ==  5 :
    n_1 , n_2  =  xyz_numeros ()
    print ( "Resultado:" , xyz_paralelo ( n_1 , n_2 ))
  elif  opcao  ==  6 :
    n_1 , n_2  =  xyz_numeros ()
    print ( "Resultado:" , xyz_potencia ( n_1 , n_2 ))
  elif  opcao  ==  0 :
    continuar  =  False
  mais :
    imprimir ( "Opcao Invalida!" )
  entrada ( "Pressione, insira para continuar" )
