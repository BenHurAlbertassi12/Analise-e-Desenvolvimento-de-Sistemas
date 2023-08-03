algoritmo "Potenciação"

var
   a, b, resultado: inteiro

inicio
   escreva("Digite o valor de a: ")
   leia(a)

   enquanto a <= 0 faca
      escreva("O valor de a deve ser positivo. Digite novamente: ")
      leia(a)
   fimenquanto

   escreva("Digite o valor de b: ")
   leia(b)

   enquanto b <= 0 faca
      escreva("O valor de b deve ser positivo. Digite novamente: ")
      leia(b)
   fimenquanto

   resultado <- 1
   para i de 1 ate b faca
      resultado <- resultado * a
   fimpara

   escreva("O resultado de ", a, " elevado a ", b, " é: ", resultado)

fimalgoritmo