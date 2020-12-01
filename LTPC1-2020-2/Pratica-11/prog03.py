def  mostrarUsuario ( nome , cpf , idade ):
    imprimir ( "Usuario:" )
    print ( "Nome:" , nome )
    imprimir ( "CPF:" , cpf )
    print ( "Idade:" , idade )
    
def  lerNovoUsuario ():
    nome  =  input ( "Nome:" )
    cpf  =  input ( "CPF:" )
    idade  =  input ( "Idade:" )
    retornar  nome , cpf , idade
    
n , c , i  =  lerNovoUsuario ()
mostrarUsuario ( n , c , i )
