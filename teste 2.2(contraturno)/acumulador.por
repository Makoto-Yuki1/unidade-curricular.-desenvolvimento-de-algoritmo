programa {
    funcao inicio() {
        inteiro N, contador, soma

        contador = 1
        soma = 0

        escreva("digite um número:")
        leia(N)

        enquanto(contador <= N) {
            soma = soma + contador
            contador = contador + 1
        }
        escreva("a soma de 1 até", N, "é:"soma)
    }
}