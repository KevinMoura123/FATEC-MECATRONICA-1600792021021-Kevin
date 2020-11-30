#Classificador de nível Gamer
#Mouse com RGB
#Teclado com RGB
#Monitor com RGB
#Mouse - Teclado - Monitor - Classificação
# sim Sim sim Viciado
# nao sim nao noia
# sim nao nao quase normal
# nao nao nao -50fps
#qualquer outro caso - não sabe responder!
mouse  =  input ( "Seu mouse tem RGB?" )
teclado  =  entrada ( "Seu teclado tem RGB?" )
monitor  =  entrada ( "Seu monitor tem RGB?" )
# = é uma ordem de educação
# == é uma pergunta de igualdade
se  mouse  ==  's'  e  teclado  ==  's'  e  monitor  ==  's' :
  imprimir ( 'Viciado!' )
#O elif é um outro condicionado. Ele vai verificar sua pergunta se uma pergunta anterior
#a ele, de um if ou outro elif, para falsa. Só executa seu bloco se a pergunta para a verdadeira
elif  mouse  ==  'n'  e  teclado  ==  's'  e  monitor  ==  'n' :
  imprimir ( 'noia' )
elif  mouse  ==  's'  e  teclado  ==  'n'  e  monitor  ==  'n' :
  imprimir ( 'quase normal' )
elif  mouse  ==  'n'  e  teclado  ==  'n'  e  monitor  ==  'n' :
  imprimir ( '-50fps' )
mais :
  print ( 'Sem classificação' )
