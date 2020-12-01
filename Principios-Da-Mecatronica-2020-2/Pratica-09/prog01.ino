const  int ENTRADA_1 = 3 ;
const  int ENTRADA_2 = 8 ;
const  int LED_1 = 12 ;
const  int LED_2 = 11 ;
const  int LED_3 = 10 ;
const  int LED_4 = 9 ;
const  int LIGADO = ALTO;
const  int DESLIGADO = LOW;
const  int ENABLE = 2 ;
const  int RS = 13 ;
const  int LCD_D7 = 7 ;
const  int LCD_D6 = 6 ;
const  int LCD_D5 = 5 ;
const  int LCD_D4 = 4 ;
const  int ECHO_PINO = A0;
const  int TRIGGER_PINO = A1;

# inclui  < LiquidCrystal.h >
// Cria uma variável chamada lcd para usar o LCD
LiquidCrystal lcd (RS, ENABLE, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

int  mede_distancia_cm () {
  digitalWrite (TRIGGER_PINO, LOW);
  atrasoMicrosegundos ( 2 );
  digitalWrite (TRIGGER_PINO, HIGH);
  atrasoMicrosegundos ( 10 );
  int tempo_da_onda = pulseIn (ECHO_PINO, HIGH);
  return  int (tempo_da_onda * 0,017 );
}

void  setup () {
  // Configurar como entradas
  pinMode (ENTRADA_1, INPUT);
  pinMode (ENTRADA_2, INPUT);
  // Configurar como critérios
  pinMode (LED_1, OUTPUT);
  pinMode (LED_2, OUTPUT);
  pinMode (LED_3, OUTPUT);
  pinMode (LED_4, OUTPUT);
  
  // Configura os pinos do sensor de distância
  pinMode (ECHO_PINO, INPUT);
  pinMode (TRIGGER_PINO, OUTPUT);
  digitalWrite (TRIGGER_PINO, HIGH);
  
  // Inicializa o LCD
  lcd. começar ( 16 , 2 );
  // Posicionar o cursor do LCD
  lcd. setCursor ( 0 , 0 ); // Coluna x Linha
  // Escrever uma msg no LCD
  lcd. print ( " Monitor Pot: " );
  
}

void  loop () {
  // Faz a leitura do potenciômetro
  int distancia = mede_distancia_cm ();
  // Limpa a linha no LCD
  lcd. limpar ();
  // Escreve a msg no LCD
  lcd. setCursor ( 0 , 1 );
  lcd. imprimir (distancia);
  lcd. imprimir ( " cm " );
  // Atualiza a msg a cada 50ms
  atraso ( 500 );
}
