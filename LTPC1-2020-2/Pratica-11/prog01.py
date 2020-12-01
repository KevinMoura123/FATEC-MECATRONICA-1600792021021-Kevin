def  semiperimetro ( a , b , c ):
    retorno ( a + b + c ) / 2
    
def  area ( a , b , c ):
    s  =  semiperímetro ( a , b , c )
    retorno ( s * ( s - a ) * ( s - b ) * ( s - c )) ** 0,5
    
a  =  float ( input ( "Lado A:" ))
b  =  float ( entrada ( "Lado B:" ))
c  =  float ( entrada ( "Lado C:" ))
area_triangulo  =  area ( a , b , c )

imprimir ( área_triangulo )
