programa{
    funcao inicio(){
        real valorc, salario, prestacao
        inteiro anos, meses 
        escreva("qual o valor da casa")
        leia (valorc)
         escreva("qual o seu salario")
         leia (salario)
          escreva("em quantos meses voccê deseja pagar")
          leia (meses)
           escreva("em quantos anos pretende pagar?")
           leia(anos)
           meses=anos * 12
           prestacao = valorc / meses

           escreva("o valor da prestação é", prestacao "\n")
se(prestacao <= salario * 0.30) {
    escreva("empréstimo aprovado \n")
} senao{
        escreva("emprestimo não aprovado " "\n")
}
    }
}