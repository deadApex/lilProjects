#include <stdio.h>
#include <stdbool.h>

int main(void){
    bool falso_ou_verdadeiro = true; //Assume apenas 0 ou 1 - True ou False
    int numero_inteiro = 10; //Assume apenas números inteiros - 32 bits
    float numero_com_ponto_flutuante = 10.5222; //Número flutuante de precisão simples - 32 bits
    double numero_flutuante_de_precisao_dupla = 10.555555555555555555555; //Número flutuante de precisão dupla - 64 bits
    char letra_qualquer = 'a'; //Armaneza um caractere simples - 8 bits
    char frase_qualquer = "abc"; //Armazena frases inteiras


    //Modificadores de Tipos de Variáveis
    unsigned int numero_inteiro_qualquer = 129; //Ignora o bit de sinal - Passa a "ter um bit a mais"
    unsigned char caracter_qualquer = "abcdef"; //Ignora o bit de sinal - Passa a "ter um bit a mais"

    signed int numero_inteiro_qualquer_2 = 127; //Implicitamente diz ao código que o bit de sinal não deve ser ignorado

    long double numero_flutuante_duplo_qualquer = 12897854548.58545484; //Aumenta a capacidade de armazenamento da variável
    long long int numero_inteiro_qualquer3 = 9223372036854775808; //Aumenta ainda mais a capacidade de armazenamento dos inteiros
}