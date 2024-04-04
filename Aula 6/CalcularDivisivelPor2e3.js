// declarar variáveis 
let numeroUm;
let numeroDois;
let numeroTres;
let numeroQuatro;
let restoDivisaoPor2;
let restoDivisaoPor3;

// iniciar variaveis 

numeroUm = 0;
numeroDois = 0;
numeroTres = 0;
numeroQuatro = 0;
restoDivisaoPor2 = 0;
restoDivisaoPor3 = 0;

// entrada de dados

numeroUm = 1;
numeroDois = 19;
numeroTres = 15; 
numeroQuatro = 24; 

// processamento 

restoDivisaoPor2 = numeroUm % 2; 
restoDivisaoPor3 = numeroUm % 3; 

// verificar se o numeroUm é divivel por 2 e 3. 

// numero 1

if (restoDivisaoPor2 == 0) { 
    if (restoDivisaoPor3 == 0) { 
        console.log ("NumeroUm [", numeroUm,"] é divisivel por 2 e 3");
    }
}
else {
    console.log ("NumeroUm [", numeroUm, "] não é divisel por 2 e 3");
} 


// numero 2
restoDivisaoPor2 = numeroDois % 2; 
restoDivisaoPor3 = numeroDois % 3; 

if (restoDivisaoPor2 == 0) { 
    if (restoDivisaoPor3 == 0) { 
        console.log ("NumeroDois [", numeroDois,"] é divisivel por 2 e 3");
    }
}

else {
    console.log ("NumeroDois [", numeroDois, "] não é divisel por 2 e 3");
} 

// numero 3

restoDivisaoPor2 = numeroTres % 2; 
restoDivisaoPor3 = numeroTres % 3; 

if (restoDivisaoPor2 == 0) { 
    if (restoDivisaoPor3 == 0) { 
        console.log ("NumeroTres [", numeroTres,"] é divisivel por 2 e 3");
    }
}
else {
    console.log ("NumeroTres [", numeroTres, "] não é divisel por 2 e 3");
} 

// numero 4

restoDivisaoPor2 = numeroQuatro % 2; 
restoDivisaoPor3 = numeroQuatro % 3; 

if (restoDivisaoPor2 == 0) { 
    if (restoDivisaoPor3 == 0) { 
        console.log ("NumeroQuatro [", numeroQuatro,"] é divisivel por 2 e 3");
    }
}
else {
    console.log ("NumeroQuatro [", numeroQuatro, "] não é divisel por 2 e 3");
} 
