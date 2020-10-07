#include <math.h>

#include <iostream>

//Função que calcula, recursivamente, o fatorial de um numero.
unsigned long int fat(int n) {
    if ((n == 1) || (n == 0))
        return 1;
    else
        return fat(n - 1) * n;
}

//Função Probabilidade de X - Distribuição Binomial
float func_probabilidade(int x, int n, float p) {
    return ((fat(n) / (fat(n - x) * fat(x))) * pow(p, x) * pow((1 - p), (n - x)));
}

int main() {
    float prob_x;   // probabilidade de ocorrer x
    float p = 0.5;  // probabilidade de ocorrer sucesso. No meu problema é 50%
    int x = 1;      // variável aleatória binomial. numero de "sucessos" em n tentativas
    int n = 10;     // numero de ensaios aleatórios independentes reproduzidos

    for (int i = 0; i < 11; i++) {
        /* code */
        prob_x = func_probabilidade(i, n, p);
        std::cout << "p(x = " << i << " ) = " << prob_x << std::endl;
    }
}