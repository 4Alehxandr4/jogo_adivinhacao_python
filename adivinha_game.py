import random # Importando a biblioteca 'random' para gerar números aleatórios

print("\n")
print(".^= =^..^= =^..^= =^..^= =^..^= =^..^= =^..^==^..^= =^..^= \n")
print("Bem vindo ao jogo de Adivinhação!")
print("...........................................................\n")

# Gerando um número secreto inteiro entre 1 e 100
numero_secreto = random.randint(1,100) 

# Inicializando as variáveis do jogo
chute = 0 
acertou = 0 
pontos = 100 # Número de pontos do usuário

# Pedindo ao usuário para escolher o nível de dificuldade
nivel = int(input(f"Qual o nível de dificuldade?\nEscolha: (1) Fácil (2) Médio (3) Difícil\n"))

# Atribuindo o número de tentativas com base no nível escolhido
if(nivel == 1):
    num_tentativa = 20
if(nivel == 2): 
    num_tentativa = 15 
if(nivel == 3): 
    num_tentativa = 6
    
tentativa = 1 # Inicializando o contador de tentativas

# O loop principal do jogo que continua enquanto a tentativa atual for menor ou igual ao número de tentativas
while tentativa <= num_tentativa: 
    print(f"Tentativa {tentativa} de {num_tentativa}")
    chute = int(input("Qual o seu chute: "))
    print(f"Seu chute foi {chute}")
    
    # Validação do chute para números fora do intervalo
    if(chute < 0 or chute > 100): 
        print("Você deve chutar um número entre 1 e 100. Tente novamente.")
        continue # Pula para a próxima iteração do loop sem contar esta tentativa
    
    # A contagem de tentativas é incrementada apenas para chutes válidos
    tentativa += 1 
    
    # Verificando se o chute está correto
    acertou = chute == numero_secreto
    
    # Cálculo de pontuação
    pontos_perdidos = abs(chute - numero_secreto)
    pontos = pontos - pontos_perdidos
    
    # Condição para quando o jogador acerta
    if(acertou):
        break # Sai do loop
    
    # Condições para quando o jogador erra e recebe uma dica
    elif(chute > numero_secreto):
        print("Você errou!\n Dica:  o número secreto é MENOR")
    elif(chute < numero_secreto):
        print("Você errou!\n Dica:  o número secreto é MAIOR")
    
# Verificando se o jogador acertou após o loop
if(acertou): 
    # Exibe a mensagem de vitória, a arte ASCII e a pontuação final
    print(f"Você acertou na tentativa {tentativa - 1}°\n")
    print("/\\_/\\ ( ")
    print("( ^.^ ) _)")
    print("\/ (      ")
    print("( | | )   ")
    print("(__d b__) ")
    print(f"Total de pontos: {pontos}") 

else: 
    # Exibe a mensagem de derrota e a arte ASCII
    print("Você perdeu! tente novamente \n")
    print(f"O número secreto era {numero_secreto}")
    print("                 /)     ")
    print("      /\\___/\\ ((      ")
    print("       \\`@_@'/ ))      ")
    print("       {_:Y:.}_//       ")
    print("       {_}^-'{_}        ")
        
    
   

