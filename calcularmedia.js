// declaracao de variaveis (x,y,r:inteiro)

// Escreva um algoritmo que calcule a média, e diga se um aluno passou ou não.

// 1 - Você deve definir quatro constantes sendo elas primeiraNota, segundaNota, terceiraNota, quartaNota.
// 2 - Atribuir uma nota de 0 até 10 para cada uma das notas Ex: const primeiraNota = 5;
// 3 - Criar uma constante chamada media, e botar a média a atribuir o valor 5, Ex: const media = 5; 
// 4 - Criar uma constante notaFinal que calcule a média da seguinte forma:
// const notaFinal = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4;
// 5 - Vai ser necessária utilizar apenas um único IF e ELSE no código.
// 6 - Vamos utilizar o operador MAIOR OU IGUAL que é representado por: >=
// 7 - Caso a condicional seja verdadeira imprimir console.log("O aluno passou");
// 8 - Caso contrário imprimir a saída com console.log("O aluno não passou");
// 9 - No final executar com node 'nome_do_arquivo.js' para vermos a execução no terminal
// 10 - Para checar com total certeza, coloque um console.log(notaFinal) no final do código e verifique se o resultado bate com o desejado.

//1 

//variaveis
const primeiraNota = 3;
const segundaNota = 3;
const terceiraNota = 3;
const quartaNota = 3;
const notaFinal=(primeiraNota+segundaNota+terceiraNota+quartaNota)/4;
const media = 5;

//processamento 
if (notaFinal<=media) {
    console.log ("o aluno não passou")
}
else {
    console.log ("o aluno passou")
}
console.log("A nota final é: " + notaFinal);

