// declarar variáveis 

let totalGanhos = 0;
let aliquotaIR = 0.0; 
let descontoIR = 0.0; 


// entrada
totalGanhos = 1500.1


// processamento 

if (totalGanhos<=500) {
    aliquotaIR = 0; 
}

else {
   if ((totalGanhos > 500.01) & (totalGanhos <= 1500)){
    aliquotaIR = 10/100;
}

else {
    if ((totalGanhos > 1500.01) & (totalGanhos <= 2500)){
    aliquotaIR = 15/100;
}

else{
    if ((totalGanhos > 2500.01)){
    aliquotaIR = 20/100;
    }
}
}
}

console.log("Aliquota é [", aliquotaIR, "] ")