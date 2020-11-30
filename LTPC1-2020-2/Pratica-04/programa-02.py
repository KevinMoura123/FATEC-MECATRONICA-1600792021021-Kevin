#Verificacao de senha
senha_secreta  =  '123456'

senha  =  input ( 'Informe a sua senha:' )

se  senha  ==  senha_secreta :
  imprimir ( 'Bem vindo Usuário' )

se  senha  ! =  senha_secreta :
  imprimir ( 'Acesso negado' )
