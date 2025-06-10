import random
import string

print("=== Gerador de Senhas Personalizado ===")

# Escolher tamanho da senha
tamanho = int(input("Digite o tamanho da senha: "))

# Perguntas ao usuário
usar_letras = input("Usar letras? (s/n): ").lower() == 's'
usar_numeros = input("Usar números? (s/n): ").lower() == 's'
usar_simbolos = input("Usar símbolos? (s/n): ").lower() == 's'

# Montar os caracteres com base nas escolhas
caracteres = ""

if usar_letras:
    caracteres += string.ascii_letters
if usar_numeros:
    caracteres += string.digits
if usar_simbolos:
    caracteres += string.punctuation

# Verifica se escolheu pelo menos uma opção
if not caracteres:
    print("Você precisa escolher pelo menos um tipo de caractere!")
else:
    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print("Senha gerada:", senha)

    # Salva em um arquivo
    salvar = input("Deseja salvar a senha em um arquivo? (s/n): ").lower()
    if salvar == 's':
        with open("senhas.txt", "a") as arquivo:
            arquivo.write(senha + "\n")
        print("Senha salva com sucesso no arquivo 'senhas.txt'.")
