abc_valores  =  "7000; 5000; 3500; 2000; 10000;"
importar  os

os . sistema ( "limpar" )
abc_posicao_inicial  =  0
abc_posicao_final  =  0
abc_contador_pev  =  0
abc_contador  =  0
abc_existe  =  False

abc_posicao_inicial_dois  =  0
abc_posicao_final_dois  =  0
abc_contador_pev_dois  =  0
abc_contador_dois  =  0
abc_existe_dois  =  False

enquanto  abc_existe  ==  False :
  abc_indicador  =  int ( input ( "Indique a posição do ';' para mostrar valor:" ))
  abc_contador_while  =  0
  para  abc_caracter  em  abc_valores :
    if  abc_caracter  ==  ";" :
      abc_contador_while  =  abc_contador_while  +  1
  if  abc_indicador  >  abc_contador_while :
    abc_existe  =  False
    print ( "nao existe" )
  mais :
    abc_existe  =  True
    print ( "existe" )

imprimir ( "" )

enquanto  abc_existe_dois  ==  False :
  abc_indicador_dois  =  int ( input ( "Agora o segundo valor:" ))
  abc_contador_while_dois  =  0
  para  abc_caracter_dois  em  abc_valores :
    if  abc_caracter_dois  ==  ";" :
      abc_contador_while_dois  =  abc_contador_while_dois  +  1
  if  abc_indicador_dois  >  abc_contador_while_dois :
    abc_existe_dois  =  False
    print ( "nao existe" )
  mais :
    abc_existe_dois  =  True
    print ( "existe" )

imprimir ( "" )

para  caracter  em  abc_valores :
  abc_contador  =  abc_contador  +  1
  se  caracter  ==  ";" :
    abc_contador_pev  =  abc_contador_pev  +  1
    se  abc_contador_pev  == ( abc_indicador  -  1 ):
      abc_posicao_inicial  =  abc_contador
    if  abc_contador_pev  ==  abc_indicador :
      abc_posicao_final  =  abc_contador

abc_valor_especifico_um  =  abc_valores [ abc_posicao_inicial :( abc_posicao_final  -  1 )]
imprimir ( abc_valor_especifico_um )
entrada ( "" )

imprimir ( "" )

para  caracter  em  abc_valores :
  abc_contador_dois  =  abc_contador_dois  +  1
  se  caracter  ==  ";" :
    abc_contador_pev_dois  =  abc_contador_pev_dois  +  1
    se  abc_contador_pev_dois  == ( abc_indicador_dois  -  1 ):
      abc_posicao_inicial_dois  =  abc_contador_dois
    if  abc_contador_pev_dois  ==  abc_indicador_dois :
      abc_posicao_final_dois  =  abc_contador_dois

abc_valor_especifico_dois  =  abc_valores [ abc_posicao_inicial_dois :( abc_posicao_final_dois  -  1 )]
imprimir ( abc_valor_especifico_dois )
entrada ( "" )

imprimir ( "" )

abc_soma  =  int ( abc_valor_especifico_um ) +  int ( abc_valor_especifico_dois )
abc_sub  =  int ( abc_valor_especifico_um ) -  int ( abc_valor_especifico_dois )
abc_mult  =  int ( abc_valor_especifico_um ) *  int ( abc_valor_especifico_dois )

imprimir ( abc_soma )
imprimir ( abc_sub )
imprimir ( abc_mult )
entrada ( "" )

# substituiçao em si
#substitui o primeiro valor indicado pela soma dos indicados
c_sub_1  =  Verdadeiro
enquanto  c_sub_1  ==  Verdadeiro :
  new_valores  =  abc_valores . substituir ( abc_valor_especifico_um , str ( abc_soma ))
  abc_valores  =  new_valores
  c_sub_1  =  False
#print (abc_valores)

#substitui o segundo valor indicado pela subtracao dos indicados
c_sub_2  =  Verdadeiro
enquanto  c_sub_2  ==  True :
  new_valores  =  abc_valores . substituir ( abc_valor_especifico_dois , str ( abc_sub ))
  abc_valores  =  new_valores
  c_sub_2  =  False
imprimir ( abc_valores )
#fazer contas com valores específicos numa string e substitui-los na mesma
