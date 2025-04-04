# Verificador de Valor de Venda Positivo

Este pequeno programa em Python tem como objetivo verificar se o valor de venda é positivo. Ele também pode ser utilizado como exemplo prático para iniciar o uso do debugger em um ambiente de desenvolvimento (IDE), como o VS Code.

## 💡 Objetivo do Código

Verificar se os valores definidos para quantidade e valor são maiores que zero, indicando uma condição de venda válida e positiva.

## 🧠 Lógica do Programa
```
quantidade = 20
valor = -30

if quantidade > 0 and valor > 0:
    print("valor positivo")
else:
    print("valor negativo")
```

Explicação passo a passo:

1) Definição de Variáveis:

* `quantidade = 20`: define que a quantidade de produtos é 20 (valor positivo).

* `valor = -30`: define que o valor de cada item é -30 (valor negativo, o que não faz sentido em uma venda real).

2) Estrutura Condicional:

* O programa verifica se ambas as variáveis (`quantidade` e `valor`) são maiores que zero.

* A condição `if quantidade > 0 and valor > 0` será falsa, pois `valor` é negativo.

* Portanto, será executado o bloco `else`, exibindo a mensagem: `"valor negativo"`.

## 🛠️ Como depurar o código (Debug) no VS Code

Você pode utilizar o depurador do VS Code para observar o comportamento do programa em tempo real. Siga os passos abaixo:

1) **Abra o menu lateral "Run and Debug"** (ou pressione `Ctrl + Shift + D`).

2) **Crie Breakpoints:**

* No editor de código, **clique à esquerda do número da linha** onde deseja que a execução pare (por exemplo, na linha do `if`).

3) **Inicie a depuração:**

* Clique no botão de "play" no topo do menu de debug.

* O código será executado até o breakpoint, permitindo que você inspecione o valor das variáveis e o fluxo de execução.

## ✅ Resultado Esperado

Como `valor = -30`, o resultado ao executar será:
```
valor negativo
```

## 📘 Conclusão

Esse programa é um exemplo simples, mas eficaz, para demonstrar:

- A utilização de **condicionais** em Python.

- Como identificar valores inválidos em uma simulação de venda.

- E como **iniciar a prática de depuração** no VS Code.

Esse tipo de análise é útil para validar dados de entrada e evitar problemas em aplicações maiores.
