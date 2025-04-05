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