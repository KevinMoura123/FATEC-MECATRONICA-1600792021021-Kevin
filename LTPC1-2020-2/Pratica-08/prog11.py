# Métodos das strings
texto  =  "a vinGAnça nunca é pLEna, MatA a aLma e envenena (Madruga, 1981)"

imprimir ( texto . maiúscula ())
imprimir ( texto . casefold ())
imprimir ( texto . contar ( "madruga" ))
texto_minusculo  =  texto . inferior ()
imprimir ( texto_minusculo )
imprimir ( texto_minusculo . count ( "madruga" ))
texto_mausculo  =  texto . superior ()
imprimir ( texto_mausculo )
imprimir ( texto_minusculo . find ( ',' ))
print ( texto_minusculo [: texto_minusculo . find ( ',' )])
