Relatório - Cálculo do IMC
=============================

Introdução:
------------
O presente relatório descreve um código Python que permite calcular o Índice de Massa Corporal (IMC) com base no peso e na altura fornecidos pelo usuário. O IMC é um indicador utilizado para avaliar a relação entre o peso e a altura de uma pessoa, permitindo a classificação em categorias de peso.

Código:
--------
O código consiste em duas funções principais:

1. Função `calcular_imc(peso, altura)`: Esta função recebe o peso (em kg) e a altura (em metros) como parâmetros e retorna o IMC, calculado através da fórmula `IMC = peso / (altura ** 2)`.

2. Função `categoria_imc(imc)`: Esta função recebe o valor do IMC calculado e retorna a categoria correspondente, de acordo com as faixas pré-definidas:

    - Abaixo do peso: IMC < 18.5
    - Peso normal: 18.5 <= IMC < 24.9
    - Sobrepeso: 25 <= IMC < 29.9
    - Obesidade grau 1: 30 <= IMC < 34.9
    - Obesidade grau 2: 35 <= IMC < 39.9
    - Obesidade grau 3: IMC >= 40

Entrada de Dados:
------------------
O código solicita ao usuário que insira seu peso (em kg) e altura (em metros) através da função `input`. As entradas são tratadas como valores float para permitir o cálculo correto do IMC.

Processamento e Saída:
-----------------------
Após receber as entradas, o código chama a função `calcular_imc` para calcular o IMC do usuário com base no peso e na altura fornecidos. Em seguida, a função `categoria_imc` é chamada para determinar a categoria correspondente ao IMC calculado.

O resultado é exibido ao usuário, apresentando o valor do IMC e a categoria na qual o IMC se enquadra.

Tratamento de Erros:
---------------------
O código trata possíveis erros ao converter as entradas do usuário para números float através de um bloco `try-except`. Caso ocorra um erro de valor inválido (por exemplo, se o usuário digitar um caractere não numérico), será exibida uma mensagem de erro informando que a entrada é inválida.

Conclusão:
------------
O código oferece uma maneira simples de calcular o IMC de um usuário com base em seu peso e altura, além de fornecer uma classificação em categorias de acordo com o resultado obtido. É importante ressaltar que o IMC é apenas um indicador, e outras informações e avaliações médicas podem ser necessárias para uma análise completa da saúde de uma pessoa.

Fim do Relatório.
=============================