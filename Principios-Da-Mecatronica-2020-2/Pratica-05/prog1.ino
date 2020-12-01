void  setup ()
{
  pinMode ( 12 , OUTPUT);
  pinMode ( 11 , OUTPUT);
  pinMode ( 10 , OUTPUT);
}

void  loop ()
{
  // Isso é um comentário de uma linha
  // Aciona como ocorre
  digitalWrite ( 12 , ALTO);
  digitalWrite ( 11 , ALTO);
  digitalWrite ( 10 , ALTO);
  // Espera 0,5 segundo
  atraso ( 500 );
  // Desliga conforme ocorre
  digitalWrite ( 12 , LOW);
  digitalWrite ( 11 , LOW);
  digitalWrite ( 10 , LOW);
  // Espera 0,5 segundo
  atraso ( 500 );
}
