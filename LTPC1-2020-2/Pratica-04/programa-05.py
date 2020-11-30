#Programa que calcula valor da parcela
valor_total  =  float ( input ( 'Valor total:' ))
numero_parcelas  =  int ( input ( 'Quantidade de parcelas:' ))

se  numero_parcelas  ==  1 :
  parcela  = ( valor_total  *  0.95 ) /  numero_parcelas
elif  numero_parcelas  ==  2 :
  parcela  =  valor_total  /  numero_parcelas
elif  numero_parcelas  ==  3 :
  parcela  = ( valor_total  *  1.05 ) /  numero_parcelas
elif  numero_parcelas  > =  4 :
  parcela  = ( valor_total  *  1.1 ) /  numero_parcelas
mais :
  imprimir ( 'omg estou chamando a policia ...' )

se  numero_parcelas  > =  1 :
  print ( 'Valor da parcela:' , parcela )
