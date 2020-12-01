def  converterF ( tempC ):
    retornar (( 9 / 5 ) * tempC ) +  32
    
def  converterK ( tempC ):
    retorno  tempC  +  273
    
temperatura_c  =  float ( input ( "Informe um valor de temp:" ))
print ( "Temp F:" , converterF ( temperatura_c ))
imprimir ( "Temp K:" , converterK ( temperatura_c ))
