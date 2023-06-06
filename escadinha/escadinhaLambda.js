function contarEscadinhas(N, sequencia) {
    if (N <= 2)
        return 1;  // Qualquer sequência com 1 ou 2 números é uma escadinha

    let diferencaAtual = sequencia[1] - sequencia[0];
    let quantidadeEscadinhas = 1;

    for (let valor = 2; valor < N; valor++) {
        if (sequencia[valor] - sequencia[valor - 1] !== diferencaAtual) {
            diferencaAtual = sequencia[valor] - sequencia[valor - 1];
            quantidadeEscadinhas++;
        }
    }

    return quantidadeEscadinhas;
}

const readline = require('readline');
// import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Informe o tamanho da sequência: ', (N) => {
    rl.question('Informe a sequência de números separados por espaço: ', (sequenciaStr) => {
        const sequencia = sequenciaStr.split(' ').map(Number);
        const resultado = contarEscadinhas(N, sequencia);
        console.log(resultado);
        rl.close();
    });
});
