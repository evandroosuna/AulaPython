// declaracao de variaveis (x,y,r:inteiro)

let numero1; 
let numero2;
let numero3;
let numero4;
let MediaPonderada;

const peso1=1;
const peso2=2;
const peso3=3;
const peso4=4;

//iniciar as variaveis

numero1 = 0;
numero2 = 0;
numero3 = 0;
numero4 = 0;

//coleta
numero1 = 4;
numero2= 7;
numero3= 3;
numero4= 25; 

peso1 = 1;
peso2 = 2;
peso3 = 3;
peso4 = 4;

// processamento
MediaPonderada = ((numero1*peso1) + (numero2*peso2) + (numero3*peso3) + (numero4*peso4)) / (1+2+3+4);

// saida
console.log(MediaPonderada); 
