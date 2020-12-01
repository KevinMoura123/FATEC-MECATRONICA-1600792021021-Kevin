def  busca ( entrada , nome_procurado ):
  encontrei  =  False
  para  nome  na  entrada . dividir ( ';' ):
    if  nome  ==  nome_procurado :
      encontrei  =  True
  retornar  encontrei

entrada  =  input ( "Informe todos os nomes, separados por ';':" )
nome  =  input ( "Informe um nome para buscar:" )

if  busca ( entrada , nome ) ==  Verdadeiro :
  imprimir ( "Encontrei!" )
mais :
  print ( "Não encontrei" )
