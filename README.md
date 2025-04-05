# Verificador de Valor de Venda Positivo (main.py)

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

## 📘 Conclusão do `main.py`

Esse programa é um exemplo simples, mas eficaz, para demonstrar:

- A utilização de **condicionais** em Python.

- Como identificar valores inválidos em uma simulação de venda.

- E como **iniciar a prática de depuração** no VS Code.

Esse tipo de análise é útil para validar dados de entrada e evitar problemas em aplicações maiores.



---

# 📄 Análise de Palavras em um Texto (main_1.py)

Este programa realiza uma análise simples de um texto, contando a quantidade de vezes que cada palavra aparece, ignorando pontuação e diferenças entre maiúsculas e minúsculas.

## 📘 Objetivo do Código

- Limpar um texto de pontuações.
- Transformar todo o conteúdo em letras minúsculas.
- Separar as palavras.
- Contar quantas vezes cada palavra aparece.
- Exibir a contagem e o total de palavras.

## 🧠 Lógica do Programa

```python
import string

# Texto original
texto = "Se o conhecimento pode criar problemas , não é através da ignorância que podemos solucioná-los. Isaac Asimov"

# Remover pontuações e colocar tudo em minúsculas
texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()

# Separar as palavras
palavras = texto_limpo.split()
print("Palavras no texto:", palavras)

# Dicionário para contar palavras
contagem_de_palavras = {}

# Contar cada palavra
for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

# Imprimir a contagem
print("\nContagem de palavras:")
for palavra, contagem in contagem_de_palavras.items():
    print(f"{palavra}: {contagem}")

# Calcular a quantidade total de palavras
total_palavras = sum(contagem_de_palavras.values())
print(f"\nTotal de palavras no texto: {total_palavras}")
```

## ✨ Explicação Detalhada

1. **Importação de `string`**:
   - Usado para acessar `string.punctuation`, que contém todos os sinais de pontuação padrão.

2. **Limpeza do texto**:
   - A função `translate()` remove as pontuações.
   - `.lower()` converte tudo para letras minúsculas.

3. **Tokenização (separar as palavras)**:
   - `.split()` quebra o texto limpo em uma lista de palavras.

4. **Contagem de Palavras**:
   - Um dicionário (`contagem_de_palavras`) é usado para armazenar a frequência de cada palavra.

5. **Exibição dos Resultados**:
   - O programa imprime a contagem de cada palavra e o total geral de palavras.

## ✅ Saída Esperada

```
Palavras no texto: ['se', 'o', 'conhecimento', 'pode', 'criar', 'problemas', 'não', 'é', 'através', 'da', 'ignorância', 'que', 'podemos', 'solucioná-los', 'isaac', 'asimov']

Contagem de palavras:
se: 1
o: 1
conhecimento: 1
pode: 1
criar: 1
problemas: 1
não: 1
é: 1
através: 1
da: 1
ignorância: 1
que: 1
podemos: 1
solucioná-los: 1
isaac: 1
asimov: 1

Total de palavras no texto: 16
```

## 📝 Conclusão do `main_1.py`

Este script é uma introdução prática à **manipulação de strings**, **dicionários** e **análise de texto**. Ele pode ser facilmente adaptado para contar palavras em textos maiores, como arquivos `.txt` ou conteúdos coletados da internet.

---

# 🧾 Validação de Entrada e Cálculo de Bônus (main_2.py)

Este programa realiza a coleta de informações do usuário (nome, salário e bônus), valida cada entrada e realiza o cálculo do valor final de um bônus com base em um KPI simplificado.

## 🎯 Objetivo do Código

Garantir que o nome digitado seja válido (sem números, espaços ou caracteres especiais).

Certificar-se de que o salário e o bônus digitados sejam valores numéricos positivos.

Calcular o valor do bônus recebido com base no salário e em um percentual informado.

Exibir uma mensagem final com os dados do usuário.

## 🧠 Lógica do Programa

```python
import string

# Inicialização das variáveis de controle
nome_valido = False
salario_valido = False
bonus_valido = False

# Solicita ao usuário que digite seu nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        
        if len(nome.strip()) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        elif any(char in string.whitespace for char in nome):
            raise ValueError("O nome não deve conter espaços.")
        elif any(char not in string.ascii_letters for char in nome):
            raise ValueError("O nome não deve conter caracteres especiais.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita o salário
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita o bônus
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido (ex: 0.1 para 10%): "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

# Cálculo do bônus
bonus_recebido = 1000 + salario * bonus

# Exibe o resultado
print(f"\\n{nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_recebido:.2f}.")
```

## ✅ Destaques

* Validação de nome com uso de `string.ascii_letters`.
* Uso de `try/except` para validação de números float.
* Simulação de KPI simples: bônus é `1000 + (salário * percentual)`.

## 🧪 Exemplo de Saída

```
Digite seu nome: john
Nome válido: john
Digite o valor do seu salário: 3000
Digite o valor do bônus recebido (ex: 0.1 para 10%): 0.2

john, seu salário é R$ 3000.00 e seu bônus final é R$ 1600.00.

```

## ✅ Conclusão do `main_2.py`

O código do `main_2.py` é um excelente exemplo de como realizar **validações robustas** de entrada de dados em Python, utilizando estruturas de repetição (`while`) combinadas com tratamento de exceções (`try/except`). A validação do nome é criteriosa, impedindo espaços, números e caracteres especiais, garantindo que o dado seja limpo e confiável.

Além disso, o código exemplifica:

- Boas práticas na coleta de dados do usuário.
- Uso de conversão de tipos com `float()` para garantir cálculos precisos.
- Lógica condicional clara para garantir que apenas valores positivos sejam aceitos.
- Um exemplo prático de **cálculo de bônus baseado em desempenho**, simulando uma regra de negócios real com KPI.

Ao final, o usuário recebe um feedback direto e formatado sobre seu salário e bônus, reforçando o aprendizado tanto em **validação** quanto em **formatação de saída**.

Esse exercício reforça a importância de tratar corretamente os dados de entrada para evitar falhas no sistema e garantir uma boa experiência para o usuário.



