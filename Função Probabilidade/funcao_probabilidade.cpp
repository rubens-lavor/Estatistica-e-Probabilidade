#include <math.h>

#include <iostream>

//Nesse exemplo uma moeda está sendo lançada aleatóriamente 10 vezes.
//X é o numero de caras.

/* Calcular:
    p(x = 0)
    p(x = 1)
    p(x = 2)
    p(x = 3)
    p(x = 4)
    p(x = 5)
    p(x = 6)
    p(x = 7)
    p(x = 8)
    p(x = 9)
    p(x = 10)
*/

//Função que calcula, recursivamente, o fatorial de um numero.
long double fat(int n) {
    if ((n == 1) || (n == 0))
        return 1;
    else
        return fat(n - 1) * n;
}

//Função Probabilidade de X - Distribuição Binomial
float func_probabilidade(int x, int n, float p) {
    return ((fat(n) / (fat(n - x) * fat(x))) * pow(p, x) * pow((1 - p), (n - x)));
}

//Distribuição de Poisson
float Poisson(int x) {
    
    return ((exp(-25.0) * pow(25, x)) /fat(x));
}

int main() {
    float prob_x;   // probabilidade de ocorrer x
    float p = 0.5;  // probabilidade de ocorrer sucesso. Neste problema é de 50%
    int x;          // variável aleatória binomial. numero de "sucessos" em n tentativas
    int n = 10;     // numero de ensaios aleatórios independentes reproduzidos
    float percent_total = 0;

    for (int x = 0; x < 11; x++) {
        prob_x = func_probabilidade(x, n, p);
        std::cout << "p(x = " << x << " ) = " << prob_x << std::endl;
        percent_total += prob_x;
    }
    std::cout << percent_total << std::endl;

    //poisson
    //Poisson(46);
    
    float p_y_leq_45 = 1;
    for (int x = 46; x < 51; x++) {
        prob_x = Poisson(x);
        std::cout << "p(x = " << x << " ) = " << prob_x << std::endl;
        p_y_leq_45 -= prob_x;
    }
    

    std::cout << "p(y<=45) = " << p_y_leq_45 << std::endl;

    return 0;
}